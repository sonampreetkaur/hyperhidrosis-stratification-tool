# Algorithmic Treatment Recommendation System for Hyperhidrosis

A mathematical clinical tool designed to algorithmically stratify hyperhidrosis patients for optimal therapeutic pathways.

## 📌 Project Overview
Patients with hyperhidrosis often face delayed access to correct clinical care due to a lack of clear triage pathways. This project bridges that gap by accepting user-inputted symptoms (severity and anatomical location), financial constraints, and compliance tolerance, then mapping them to standardized medical intervention tiers.

## 🛠️ Tech Stack & Methodology
* *Language:* Python 3
* *Environment:* Developed and validated within Google Colab
* *Data Visualization:* Matplotlib (renders dynamic vertical compatibility charts)
* *Core Logic:* Conditional branching arrays (if-elif-else loops) backed by absolute clinical safety overrides.

## ⚙️ How It Works
1. *Data Acquisition:* The tool prompts the user to input symptom severity (mild/moderate/severe), focal location, budget capacity, and treatment compliance tolerance.
2. *Algorithmic Processing:* Inputs are evaluated against a standardized treatment matrix using an additive point system.
3. *Clinical Safety Overrides (Exclusion Thresholds):* 
   * *Financial Constraint:* Premium therapies (e.g., Botox) are immediately forced to a 0% match if a user specifies a low budget.
   * *Medical Safety:* High-risk, irreversible interventions (e.g., ETS Surgery) are automatically forced to a 0% match if symptom severity is mild.
4. *Data Visualization:* Matplotlib automatically generates a tiered bar chart mapping patient compatibility against the four clinical intervention tiers.

## 🚀 Quick Start & Usage
1. Open the code file inside your [Google Colab Workspace](https://google.com).
2. Execute the notebook cell to launch the interactive command-line interface.
3. Input your clinical metrics to generate your personalized Patient Stratification Analysis Matrix graph.
