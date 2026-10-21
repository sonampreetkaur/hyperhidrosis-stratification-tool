# 🩺 Hyperhidrosis Stratification Tool (HST) — Version 4.1

An interactive, rule-based medical decision-support dashboard built in Python to algorithmically evaluate and visualize treatment pathway compatibilities for patients experiencing pathological excessive sweating (hyperhidrosis).

---

## 🤖 Engineering & Artificial Intelligence Disclosure
This application was engineered by translating raw data analysis concepts into a functional web software interface. *Generative Artificial Intelligence was actively leveraged as a collaborative coding partner* to assist in optimizing structural code formatting, debugging deployment configurations, and accelerating the implementation of advanced visualization frameworks (Streamlit and Plotly Express). This project showcases code literacy, prompt engineering proficiency, and the ability to critically review, refactor, and deploy AI-assisted logic into a working, real-world prototype.

---

## 📊 Complete Technical & Code Architecture Breakdown

The application processes user-inputted clinical vectors (symptoms, history, preferences) through a static multi-parameter matrix to compute personalized suitability scores.

### 1. Ingestion Layer (User Interface)
The app captures two primary streams of patient metrics using reactive Streamlit web components:
* *Demographics & Thresholds:* Gathers categorical vectors for Symptom Severity (Mild/Moderate/Severe), Main Location Affected (Palmar/Plantar/Both), Financial Capacity (Low/High), and individual patient tolerance levels across systemic medication, treatment compliance burden, and surgical risk profiles.
* *Historical Matrix:* Maps prior clinical experience across five standard therapeutic interventions using horizontal radio select options: Not Tried, Adequate, Inadequate, or Intolerable.

### 2. Algorithmic Matching Logic (calculate_compatibility)
The backend matches patient vectors against hardcoded optimal treatment profiles:
* *Topical Treatment:* Optimized for low baseline compliance burden, low surgical risk tolerance, and general severity profiles.
* *Iontophoresis:* Mapped primarily for local palmar/plantar areas with capacity for high mechanical treatment compliance burdens.
* *Oral Medications:* Configured specifically for multi-focal/generalized presentations with a structural requirement for high systemic oral medication tolerance.
* *Botulinum Toxin:* Gated for severe/moderate localized presentations matched with high financial capacities due to recurrent clinical costs.
* *ETS (Endoscopic Thoracic Sympathectomy):* Strictly limited to isolated severe upper-extremity conditions with high surgical intervention tolerance.

*Mathematical Scoring Formula:*
The algorithm aggregates structural matches across five core fields plus a conditional sixth parameter for systemic requirements. The base percentage is generated uniformly:
\[\text{Compatibility Score} = \left( \frac{\text{Total Profile Matches}}{\text{Total Available Variables (6)}} \right) \times 100\]

### 3. Historical Penalty Offsets (history_penalty)
To ensure clinical realism, the script modifies the ideal compatibility score by evaluating a patient's historical response to that specific treatment tier:
* Not Tried or Adequate = *0% Deduction*
* Inadequate Response = *-30% Penalty Deduction*
* Intolerable Side Effects = *-40% Penalty Deduction*

\[\text{Adjusted Score} = \max(0, \text{Compatibility Score} - \text{Historical Penalty})\]

### 4. Hard Structural Safety Gates (ets_constraint)
The script implements an absolute computational clinical safety override for the most invasive surgical path (*ETS* — Thoracic Sympathectomy). The script evaluates the surgical intervention as a closed system loop. 

Even if a patient's base preference matches a surgical profile, the algorithm flags the pathway as *"Excluded" (0% Score)* unless the patient meets all three strict parameters:
1. Presents with *Severe* symptoms localized to *Palmar* or *Both* regions.
2. Demonstrates documented therapeutic failure (Inadequate or Intolerable) across *at least one* conservative foundational tier (Topical Treatments, Iontophoresis, or Oral Medication).
3. Expressly indicates a *High* overall surgical risk tolerance.

This structural safeguard models real-world medical ethics, ensuring irreversible surgical intervention is programmatically restricted until safer conservative options are exhausted.

### 5. Data Layer & Visualization Matrix
* *Data Frames:* The calculated results are converted into an on-the-fly pandas.DataFrame grouping treatments by their final score and conditional "Active" vs "Excluded" flags.
* *Plotly Analytics Matrix:* Renders a dynamic, client-side graphical bar chart utilizing plotly.express. Bars are mapped using conditional colors (Navy blue for actively matched options; Crimson red for systems-excluded interventions) displaying clear, responsive overlay labels.

---

## 🛠️ Local Development & Deployment Installation
To launch this project locally on your machine, deploy the custom execution script or initialize via command interface:

bash
# Clone the repository
git clone https://github.com

# Install package dependencies 
pip install -r requirements.txt

# Run the reactive web framework
streamlit run app.py
