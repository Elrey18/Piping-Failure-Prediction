import streamlit as st
from src.utils import render_sidebar


# -------------------------
# Page Configuration
# -------------------------
st.set_page_config(
    page_title="Pipeline Integrity AI",
    page_icon="🛢️",
    layout="wide",
    initial_sidebar_state="expanded"
)

render_sidebar()


# -------------------------
# Main Header
# -------------------------
st.title("🛢️ Pipeline Integrity AI")

st.subheader("Predictive Maintenance & Condition Assessment System")

st.markdown("---")


# -------------------------
# Hero Section
# -------------------------
left, right = st.columns([2, 1])

with left:
    st.markdown("""
### Welcome

**Pipeline Integrity AI** is a machine learning-powered decision support system
designed to assist engineers in evaluating the condition of oil and gas pipelines.

The system uses inspection and operating parameters to classify pipeline condition as:

- 🟢 **Normal**
- 🟡 **Moderate**
- 🔴 **Critical**

The final model uses a trained **Random Forest Classifier**.
""")

with right:
    st.metric("Model Accuracy", "92.5%")
    st.metric("Pipeline Classes", "3")
    st.metric("ML Algorithm", "Random Forest")


st.divider()


# -------------------------
# System Features
# -------------------------
st.header("System Features")

c1, c2, c3 = st.columns(3)

with c1:
    st.success("""
### 🔍 Inspection

Input pipeline inspection measurements and generate AI condition predictions.
""")

with c2:
    st.info("""
### 📊 Dashboard

Visualize risk level, confidence, probabilities, and inspection history.
""")

with c3:
    st.warning("""
### 📄 Reports

Generate downloadable engineering inspection reports in PDF format.
""")


st.divider()


# -------------------------
# Workflow
# -------------------------
st.header("Recommended Workflow")

step1, step2, step3 = st.columns(3)

with step1:
    st.markdown("""
### 1️⃣ Inspect

Go to the **Inspection** page and enter pipeline data.
""")

with step2:
    st.markdown("""
### 2️⃣ Analyze

Open the **Dashboard** page to view condition, risk, and probability charts.
""")

with step3:
    st.markdown("""
### 3️⃣ Report

Generate a downloadable PDF report from the **Reports** page.
""")


st.divider()


# -------------------------
# Project Overview
# -------------------------
st.header("Project Overview")

st.write("""
This application uses Inspection parameters such as Pipe size, Thickness,
Pressure, Temperature, Corrosion impact, Material loss, Material type, and Pipe grade
to estimate the operational condition of an Oil and Gas pipeline.

The project demonstrates a complete machine learning workflow:

- Exploratory Data Analysis
- Feature Engineering
- Random Forest Classification
- Model Evaluation
- Streamlit Application Development
- PDF Report Generation
""")

st.info("Use the sidebar to navigate through the application.")