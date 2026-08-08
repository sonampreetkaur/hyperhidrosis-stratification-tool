import matplotlib.pyplot as plt

# 1. The Stratification Framework stored as a Dictionary
treatment_matrix = {
    "Tier 1: Topical Therapy": {"severity": "mild", "location": "both", "budget": "low", "compliance": "low"},
    "Tier 2: Iontophoresis": {"severity": "moderate", "location": "both", "budget": "low", "compliance": "high"},
    "Tier 3: Botox Injections": {"severity": "severe", "location": "palmar", "budget": "high", "compliance": "low"},
    "Tier 4: ETS Surgery": {"severity": "severe", "location": "both", "budget": "high", "compliance": "high"}
}

# 2. Interactive User Interface (Collecting Inputs)
print("=========================================================")
print("  PRIMARY HYPERHIDROSIS THERAPEUTIC STRATIFICATION TOOL  ")
print("=========================================================")
print("\nPlease enter your clinical details below:\n")

user_sev = input("1. Enter symptom severity (mild / moderate / severe): ").strip().lower()
user_loc = input("2. Enter focal location (palmar / plantar / both): ").strip().lower()
user_bud = input("3. Enter your budget capacity (low / high): ").strip().lower()
user_com = input("4. Enter daily treatment compliance tolerance (low / high): ").strip().lower()

search_loc = "both" if user_loc == "both" else user_loc

# 3. Computational Decision Tree Logic (Calculating Match Scores)
compatibility_scores = {}

for tier, criteria in treatment_matrix.items():
    match_points = 0
    if criteria["severity"] == user_sev: match_points += 1
    if criteria["location"] == "both" or criteria["location"] == search_loc: match_points += 1
    if criteria["budget"] == user_bud: match_points += 1
    if criteria["compliance"] == user_com: match_points += 1
    
    # Calculate baseline score percentage
    final_score = (match_points / 4) * 100
    
    # -----------------------------------------------------------------
    # CRITICAL CLINICAL SAFETY OVERRIDES (Absolute Exclusions)
    # -----------------------------------------------------------------
    # 1. Budget Exclusion: Low budget patients cannot be recommended high-cost treatments
    if user_bud == "low" and criteria["budget"] == "high":
        final_score = 0
        
    # 2. Severity/Safety Exclusion: Mild cases can never be recommended permanent surgery (Tier 4)
    if user_sev == "mild" and tier == "Tier 4: ETS Surgery":
        final_score = 0
    # -----------------------------------------------------------------
    
    compatibility_scores[tier] = final_score

# 4. Data Visualization Output using Matplotlib
print("\nProcessing clinical features... Generating compatibility graph...")

plt.figure(figsize=(10, 5))
colors = ['#5dade2', '#58d68d', '#ec7063', '#af7ac5']

bars = plt.bar(compatibility_scores.keys(), compatibility_scores.values(), color=colors, edgecolor='grey', width=0.6)

plt.ylabel('Treatment Compatibility Score (%)', fontsize=12, fontweight='bold')
plt.title('Patient Stratification Analysis Matrix', fontsize=14, fontweight='bold', pad=15)
plt.ylim(0, 110)
plt.grid(axis='y', linestyle='--', alpha=0.5)

for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2.0, yval + 2, f"{int(yval)}%", ha='center', va='bottom', fontweight='bold')

plt.tight_layout()
plt.show()
