# Pipeline Failure Prediction using Machine Learning

## Project Overview

This project applies Machine Learning techniques to predict pipeline conditions using sensor and inspection data. The objective is to classify pipelines into:

- Normal
- Moderate
- Critical

The project demonstrates an end-to-end Machine Learning workflow including:

- Data Cleaning
- Exploratory Data Analysis (EDA)
- Feature Engineering
- Data Preprocessing
- Random Forest Classification
- XGBoost Classification
- Model Evaluation
- Explainable AI using SHAP

---

# Business Problem

Pipeline failures can lead to:

- Environmental pollution
- Production downtime
- Expensive maintenance
- Safety incidents

Being able to identify deteriorating pipelines before failure allows engineers to prioritize inspections and implement predictive maintenance strategies.

---

# Dataset

The dataset contains pipeline inspection and operating information including:

| Feature | Description |
|----------|-------------|
| Pipe_Size_mm | Pipeline outside diameter |
| Thickness_mm | Original wall thickness |
| Material | Pipe construction material |
| Grade | Material grade/specification |
| Max_Pressure_psi | Maximum operating pressure |
| Temperature_C | Operating temperature |
| Corrosion_Impact_Percent | Estimated corrosion impact |
| Thickness_Loss_mm | Measured wall thickness loss |
| Material_Loss_Percent | Estimated percentage material loss |
| Time_Years | Pipeline age |
| Condition | Target variable |

Target Classes

- Normal
- Moderate
- Critical

---

# Exploratory Data Analysis

EDA included:

- Distribution analysis
- Correlation heatmap
- Boxplots
- Outlier detection
- Class balance analysis

Major findings:

- Thickness Loss and Material Loss increase significantly with pipeline deterioration.
- Pressure, Temperature and Age showed comparatively lower predictive capability.
- Approximately 10.1% of observations contained physically inconsistent values where Thickness Loss exceeded original Thickness.

---

# Data Preprocessing

The preprocessing workflow included:

- One-Hot Encoding of categorical variables
- Label Encoding of target variable
- Stratified Train/Test Split
- Standardization of numerical variables

Training/Test Split:

- Training: 800 observations
- Testing: 200 observations

---

# Models

Two models were developed.

## Random Forest

Accuracy:

92.5%

Performance:

- Critical Recall: 93%
- Critical Precision: 97%

---

## XGBoost

Accuracy:

90.5%

Random Forest produced better overall performance and was selected as the final model.

---

# Model Explainability

SHAP (SHapley Additive Explanations) was used to explain model predictions.

The most influential features were:

1. Thickness_Loss_mm
2. Material_Loss_Percent
3. Thickness_mm

The SHAP analysis confirmed that increasing wall thickness loss strongly increased the likelihood of predicting a Critical pipeline condition.

---

# Results

Final Model:

Random Forest Classifier

Performance Summary:

| Metric | Value |
|---------|--------|
| Accuracy | 92.5% |
| Precision | 93% |
| Recall | 93% |
| F1 Score | 93% |

---

# Business Impact

This model demonstrates how Machine Learning can support predictive maintenance by:

- Prioritizing high-risk pipelines
- Supporting inspection planning
- Reducing unexpected failures
- Improving pipeline integrity management

---

# Limitations

This dataset appears to be synthetically generated.

Approximately 10.1% of records contained physically inconsistent measurements where Thickness Loss exceeded original Thickness.

These records were retained to preserve the original dataset but would require engineering validation before deployment in a production environment.

---

# Future Improvements

Possible improvements include:

- Hyperparameter optimization
- Cross Validation
- Probability-based risk scoring
- Time-series sensor monitoring
- Real-world SCADA integration
- Deployment using Streamlit or Flask

---

# Technologies Used

Python

Pandas

NumPy

Matplotlib

Seaborn

Scikit-Learn

XGBoost

SHAP

Jupyter Notebook

---

# Author

**Muhammad Aminu Aliyu**

Petroleum Engineer | Data Analyst | Machine Learning Enthusiast

LinkedIn:
https://www.linkedin.com/in/muhammad-aminu-aliyu-6068b728b/

Email:
ameenuabs!@gmail.com
