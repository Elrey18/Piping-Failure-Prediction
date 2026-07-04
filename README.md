# Pipeline Integrity AI

## Predictive Maintenance & Condition Assessment System

Pipeline Integrity AI is a machine learning-powered web application designed to support oil and gas pipeline condition assessment and predictive maintenance decision-making.

The system predicts whether a pipeline is:

- 🟢 Normal
- 🟡 Moderate
- 🔴 Critical

using inspection, operating, and material-related pipeline data.

---

## Project Objective

Pipeline failures can lead to environmental pollution, production downtime, safety incidents, and costly repairs. This project demonstrates how machine learning can assist engineers in identifying high-risk pipelines and prioritizing maintenance actions.

---

## Key Features

- Interactive Streamlit web application
- Pipeline condition prediction using Random Forest
- Dynamic health dashboard
- Prediction confidence display
- Class probability distribution
- Inspection history table
- Downloadable PDF inspection report
- Engineering maintenance recommendations
- Multi-page professional interface

---

## Machine Learning Workflow

The project follows a complete machine learning workflow:

1. Data loading and inspection
2. Exploratory Data Analysis
3. Engineering data validation
4. Categorical encoding
5. Feature scaling
6. Random Forest model training
7. XGBoost model comparison
8. Model evaluation
9. SHAP explainability
10. Streamlit application development
11. PDF report generation

---

## Dataset Features

The model uses the following input features:

- Pipe size
- Pipe thickness
- Maximum pressure
- Temperature
- Corrosion impact
- Thickness loss
- Material loss
- Pipeline age
- Material type
- Pipe grade

---

## Model Performance

Final selected model:

**Random Forest Classifier**

Performance summary:

| Metric | Value |
|---|---:|
| Accuracy | 92.5% |
| Critical Precision | 97% |
| Critical Recall | 93% |

Random Forest was selected because it outperformed XGBoost on the test set while remaining easier to interpret and deploy.

---

## Explainability

SHAP was used to explain model predictions and identify the strongest drivers of pipeline condition.

The most important features were:

1. Thickness Loss
2. Material Loss Percentage
3. Pipe Thickness
4. Pipe Size

This aligns with engineering expectations that structural deterioration indicators are strong predictors of pipeline integrity risk.

---

## Project Structure

```text
piping-failure-prediction/
│
├── app.py
├── README.md
├── requirements.txt
├── .gitignore
├── data/
├── models/
├── src/
├── pages/
├── assets/
├── notebooks/
└── reports/