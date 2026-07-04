import streamlit as st
import plotly.graph_objects as go
import pandas as pd
from src.utils import render_sidebar, apply_custom_style


st.set_page_config(
    page_title="Dashboard",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

apply_custom_style()
render_sidebar()


st.title("📊 Pipeline Health Dashboard")

st.write("Dashboard updates based on the latest inspection prediction.")

st.divider()


last_prediction = st.session_state.get("last_prediction", None)

if last_prediction is None:

    st.warning(
        "No inspection prediction found yet. Go to the Inspection page and run a prediction first."
    )

    prediction = "Normal"
    confidence = 0
    probabilities = {
        "Critical": 0,
        "Moderate": 0,
        "Normal": 0,
    }

    input_data = {
        "Corrosion_Impact_Percent": 0,
        "Material_Loss_Percent": 0,
        "Thickness_Loss_mm": 0,
        "Max_Pressure_psi": 0,
        "Temperature_C": 0,
        "Time_Years": 0,
    }

else:

    prediction = last_prediction["prediction"]
    confidence = last_prediction["confidence"]
    probabilities = last_prediction["probabilities"]
    input_data = last_prediction["input_data"]


if prediction == "Normal":
    health_score = 90

elif prediction == "Moderate":
    health_score = 60

else:
    health_score = 25


risk_level = {
    "Normal": "LOW",
    "Moderate": "MEDIUM",
    "Critical": "HIGH"
}.get(prediction, "UNKNOWN")


col1, col2, col3, col4 = st.columns(4)

col1.metric("Pipeline Health", f"{health_score}%")
col2.metric("Risk Level", risk_level)
col3.metric("AI Confidence", f"{confidence:.2f}%")
col4.metric("Predicted Condition", prediction)

st.divider()


g1, g2 = st.columns(2)

with g1:
    health_gauge = go.Figure(
        go.Indicator(
            mode="gauge+number",
            value=health_score,
            title={"text": "Pipeline Health (%)"},
            gauge={
                "axis": {"range": [0, 100]},
                "bar": {
                    "color": "green"
                    if health_score >= 70
                    else "orange"
                    if health_score >= 40
                    else "red"
                },
                "steps": [
                    {"range": [0, 40], "color": "#ffcccc"},
                    {"range": [40, 70], "color": "#fff2cc"},
                    {"range": [70, 100], "color": "#d9ead3"},
                ],
            },
        )
    )

    st.plotly_chart(health_gauge, use_container_width=True)


with g2:
    confidence_gauge = go.Figure(
        go.Indicator(
            mode="gauge+number",
            value=confidence,
            title={"text": "Model Confidence (%)"},
            gauge={
                "axis": {"range": [0, 100]},
                "bar": {"color": "blue"},
                "steps": [
                    {"range": [0, 50], "color": "#f4cccc"},
                    {"range": [50, 80], "color": "#fff2cc"},
                    {"range": [80, 100], "color": "#cfe2f3"},
                ],
            },
        )
    )

    st.plotly_chart(confidence_gauge, use_container_width=True)


st.subheader("Prediction Probability Distribution")

prob_df = pd.DataFrame(
    {
        "Condition": list(probabilities.keys()),
        "Probability (%)": list(probabilities.values()),
    }
)

prob_chart = go.Figure(
    go.Bar(
        x=prob_df["Condition"],
        y=prob_df["Probability (%)"],
    )
)

prob_chart.update_layout(
    xaxis_title="Condition",
    yaxis_title="Probability (%)",
    yaxis=dict(range=[0, 100])
)

st.plotly_chart(prob_chart, use_container_width=True)


st.subheader("Inspection Indicators")

indicator_data = pd.DataFrame(
    {
        "Parameter": [
            "Corrosion Impact (%)",
            "Material Loss (%)",
            "Thickness Loss (mm)",
            "Pressure (psi)",
            "Temperature (°C)",
            "Age (Years)",
        ],
        "Value": [
            input_data.get("Corrosion_Impact_Percent", 0),
            input_data.get("Material_Loss_Percent", 0),
            input_data.get("Thickness_Loss_mm", 0),
            input_data.get("Max_Pressure_psi", 0),
            input_data.get("Temperature_C", 0),
            input_data.get("Time_Years", 0),
        ],
    }
)

st.dataframe(indicator_data, use_container_width=True)


st.subheader("Inspection History")

history = st.session_state.get("inspection_history", [])

if history:
    history_df = pd.DataFrame(history)
    st.dataframe(history_df, use_container_width=True)

else:
    st.info("No inspection history available yet.")


st.subheader("AI Recommendation")

if prediction == "Normal":
    st.success("""
✅ Continue routine inspection.

✅ No urgent intervention required.

✅ Maintain normal monitoring schedule.
""")

elif prediction == "Moderate":
    st.warning("""
⚠ Increase inspection frequency.

⚠ Monitor corrosion and material loss trends.

⚠ Plan preventive maintenance.
""")

else:
    st.error("""
🚨 Immediate engineering attention required.

🚨 Inspect the pipeline section urgently.

🚨 Consider repair, replacement, or shutdown depending on operational risk.
""") 