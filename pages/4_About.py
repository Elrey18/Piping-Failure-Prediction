import streamlit as st
from src.utils import render_sidebar, apply_custom_style


st.set_page_config(
    page_title="About",
    page_icon="ℹ️",
    layout="wide",
    initial_sidebar_state="expanded"
)

apply_custom_style()
render_sidebar()


st.title("ℹ️ About Pipeline Integrity AI")

st.subheader("Predictive Maintenance & Condition Assessment System")

st.divider()


st.header("Project Description")

st.write("""
Pipeline Integrity AI is a machine learning-powered application developed to support
pipeline condition assessment and predictive maintenance decision-making.

The application uses pipeline inspection and operating data to classify pipeline condition as:

- 🟢 Normal
- 🟡 Moderate
- 🔴 Critical

The project demonstrates how petroleum engineering knowledge can be combined with
data analytics and machine learning to support asset integrity management.
""")


st.header("Machine Learning Workflow")

st.markdown("""
The project followed a complete machine learning workflow:

1. Data loading and inspection  
2. Exploratory Data Analysis  
3. Engineering data validation  
4. Feature preprocessing  
5. Random Forest model training  
6. XGBoost model comparison  
7. Model evaluation  
8. SHAP explainability  
9. Streamlit app deployment  
10. PDF report generation  
""")


st.header("Key Model Results")

c1, c2, c3 = st.columns(3)

with c1:
    st.metric("Final Model", "Random Forest")

with c2:
    st.metric("Accuracy", "92.5%")

with c3:
    st.metric("Critical Recall", "93%")


st.header("Key Predictive Features")

st.markdown("""
The most important predictors identified during model development were:

- Thickness Loss
- Material Loss Percentage
- Pipe Thickness
- Pipe Size
- Corrosion Impact
""")


st.header("Engineering Relevance")

st.write("""
Pipeline failures can lead to production downtime, environmental damage, safety incidents,
and expensive repair operations. This application demonstrates how machine learning can help
prioritize inspection and maintenance decisions.

The system is intended as a decision-support tool and should be used together with professional
engineering judgment and field validation.
""")


st.header("Developer")

st.write("""
**Muhammad Aminu Aliyu**  
Petroleum Engineer | Data Analyst | Machine Learning Enthusiast

This project was built as a portfolio project to demonstrate the Application of Machine Learning
to Oil and Gas pipeline integrity management.
""")


st.info(
    "This application is for educational and portfolio demonstration purposes."
)