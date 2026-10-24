import streamlit as st
import plotly.express as px
import pandas as pd

# ============================================================
# HYPERHIDROSIS STRATIFICATION TOOL (HST) - WEB VERSION 4.1
# ============================================================

st.set_page_config(page_title="Hyperhidrosis Stratification Tool", layout="wide")

st.title("🩺 Hyperhidrosis Stratification Tool (HST)")
st.caption("Version 4.1 - Rule-Based Treatment Compatibility Prototype")

st.warning(
    "⚠️ *IMPORTANT NOTICE:* This tool provides a preliminary algorithmic comparison of selected treatment pathways. "
    "It is NOT a medical diagnosis, clinical recommendation, or proxy for efficacy. "
    "Treatment decisions must always be discussed with a qualified healthcare professional."
)

st.markdown("---")
st.markdown("### 📊 Patient Case Profiles & Preferences")
col1, col2 = st.columns(2)

with col1:
    st.info("🧬 *Demographics & Symptoms*")
    severity = st.selectbox("Symptom Severity", ["Mild", "Moderate", "Severe"], key="pref_severity").lower()
    location = st.selectbox("Main Location Affected", ["Palmar", "Plantar", "Both"], key="pref_location").lower()
    budget = st.selectbox("Financial / Budget Capacity", ["Low", "High"], key="pref_budget").lower()

    st.info("🧠 *Patient Tolerances*")
    treatment_burden = st.selectbox("Tolerance for Treatment Burden / Compliance", ["Low", "High"], key="pref_burden").lower()
    risk_tolerance = st.selectbox("Tolerance for Treatment Risk / Invasiveness", ["Low", "High"], key="pref_risk").lower()
    systemic_tolerance = st.selectbox("Tolerance for Systemic (Oral) Medications", ["Low", "High"], key="pref_systemic").lower()

with col2:
    st.info("⏳ *Previous Treatment History & Patient Responses*")
    st.markdown("Select how the patient historically responded to these pathways if attempted:")
    
    treatments = ["Topical treatment", "Iontophoresis", "Oral medication", "Botulinum toxin", "ETS"]
    history = {}
    
    for t in treatments:
        history[t] = st.radio(
            f"*{t}*", 
            ["Not Tried", "Adequate", "Inadequate", "Intolerable"], 
            horizontal=True,
            key=f"hist_{t.lower().replace(' ', '_')}"
        ).lower().replace(" ", "_")

# Core Profiles & Variables
profiles = {
    "Topical treatment": {"location": ["palmar", "plantar", "both"], "severity": ["mild", "moderate", "severe"], "budget": ["low", "high"], "burden": ["low"], "risk": ["low"], "systemic_required": False},
    "Iontophoresis": {"location": ["palmar", "plantar", "both"], "severity": ["moderate", "severe"], "budget": ["low", "high"], "burden": ["high"], "risk": ["low"], "systemic_required": False},
    "Oral medication": {"location": ["palmar", "plantar", "both"], "severity": ["moderate", "severe"], "budget": ["low", "high"], "burden": ["high"], "risk": ["low", "high"], "systemic_required": True},
    "Botulinum toxin": {"location": ["palmar", "plantar", "both"], "severity": ["moderate", "severe"], "budget": ["high"], "burden": ["low"], "risk": ["high"], "systemic_required": False},
    "ETS": {"location": ["palmar", "both"], "severity": ["severe"], "budget": ["high"], "burden": ["high"], "risk": ["high"], "systemic_required": False}
}

history_penalty = {"not_tried": 0, "adequate": 0, "inadequate": 30, "intolerable": 40}

def calculate_compatibility(profile):
    points = 0
    if location in profile["location"]: points += 1
    if severity in profile["severity"]: points += 1
    if budget in profile["budget"]: points += 1
    if treatment_burden in profile["burden"]: points += 1
    if risk_tolerance in profile["risk"]: points += 1
    
    if profile["systemic_required"]:
        if systemic_tolerance == "high": points += 1
    else:
        points += 1
        
    return (points / 6) * 100

def ets_constraint():
    previous_failure = any(history[t] in ["inadequate", "intolerable"] for t in ["Topical treatment", "Iontophoresis", "Oral medication"])
    return severity == "severe" and location in ["palmar", "both"] and previous_failure and risk_tolerance == "high"

results = {}
for treatment, profile in profiles.items():
    compatibility = calculate_compatibility(profile)
    status = history[treatment]
    penalty = history_penalty.get(status, 0)
    adjusted_score = max(0, compatibility - penalty)
    excluded = False

    if treatment == "ETS" and not ets_constraint():
        excluded = True
        adjusted_score = 0

    results[treatment] = {"adjusted": adjusted_score, "excluded": excluded}

st.markdown("---")
st.markdown("### 📈 Algorithmic Pathway Matrix")

df = pd.DataFrame([
    {"Treatment": t, "Score": r["adjusted"], "Status": "Excluded" if r["excluded"] else "Active"} 
    for t, r in results.items()
])

chart_col, notes_col = st.columns(2)

with chart_col:
    fig = px.bar(
        df, 
        x="Treatment", 
        y="Score", 
        text=df["Score"].apply(lambda x: f"{x:.1f}%"),
        color="Status",
        color_discrete_map={"Active": "#2b5c8f", "Excluded": "#d9534f"},
        labels={"Score": "Algorithmic Compatibility (%)"}
    )
    fig.update_layout(yaxis_range=[0, 110], showlegend=False)
    st.plotly_chart(fig, use_container_width=True)

with notes_col:
    st.markdown("#### *System Diagnostics & Exclusions*")
    for t, r in results.items():
        if r["excluded"]:
            st.error(f"❌ *{t}*: Dropped via system clinical constraint.")
        else:
            st.success(f"✅ *{t}: Matched at *{r['adjusted']:.1f}%**")
            st.markdown("---")
st.subheader("💬 Clinical Logic & UX Feedback")
st.write("Help refine this independent research tool! As a gap-year student, your insights help me improve this decision-tree logic workflow.")
st.info("👉 [Click here to share your feedback in a quick anonymous form](https://forms.gle/7WrPnkauozfviTby7)")
