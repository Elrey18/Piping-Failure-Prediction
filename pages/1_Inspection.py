import streamlit as st
from src.predictor import predict_pipeline
from src.utils import render_sidebar, display_condition_result, display_recommendation, apply_custom_style


st.set_page_config(
    page_title="Pipeline Inspection",
    page_icon="🔍",
    layout="wide",
    initial_sidebar_state="expanded"
)

apply_custom_style()
render_sidebar()


st.title("🔍 Pipeline Inspection")

st.write(
    "Enter pipeline inspection and operating data below to predict the pipeline condition."
)

st.divider()


left, right = st.columns(2)

with left:
    st.subheader("Pipeline Design & Operating Data")

    pipe_size = st.number_input(
        "Pipe Size (mm)",
        min_value=50.0,
        value=500.0
    )

    thickness = st.number_input(
        "Thickness (mm)",
        min_value=1.0,
        value=12.0
    )

    pressure = st.number_input(
        "Maximum Pressure (psi)",
        value=1000.0
    )

    temperature = st.number_input(
        "Temperature (°C)",
        value=30.0
    )

with right:
    st.subheader("Integrity & Degradation Data")

    corrosion = st.slider(
        "Corrosion Impact (%)",
        0.0,
        100.0,
        10.0
    )

    thickness_loss = st.number_input(
        "Thickness Loss (mm)",
        value=1.0
    )

    material_loss = st.slider(
        "Material Loss (%)",
        0.0,
        100.0,
        10.0
    )

    age = st.number_input(
        "Pipeline Age (Years)",
        value=5.0
    )


st.divider()

material_col, grade_col = st.columns(2)

with material_col:
    material = st.selectbox(
        "Material",
        [
            "Carbon Steel",
            "Stainless Steel",
            "PVC",
            "HDPE",
            "Fiberglass"
        ]
    )

with grade_col:
    grade = st.selectbox(
        "Grade",
        [
            "API 5L X42",
            "API 5L X52",
            "API 5L X65",
            "ASTM A106 Grade B",
            "ASTM A333 Grade 6"
        ]
    )


st.divider()


if st.button("Predict Pipeline Condition", use_container_width=True):

    input_data = {
        "Pipe_Size_mm": pipe_size,
        "Thickness_mm": thickness,
        "Max_Pressure_psi": pressure,
        "Temperature_C": temperature,
        "Corrosion_Impact_Percent": corrosion,
        "Thickness_Loss_mm": thickness_loss,
        "Material_Loss_Percent": material_loss,
        "Time_Years": age,
        "Material": material,
        "Grade": grade,
    }

    prediction, confidence, probabilities = predict_pipeline(input_data)

    st.session_state["last_prediction"] = {
        "prediction": prediction,
        "confidence": confidence,
        "probabilities": probabilities,
        "input_data": input_data,
    }

    if "inspection_history" not in st.session_state:
        st.session_state["inspection_history"] = []

    st.session_state["inspection_history"].append(
        {
            "Prediction": prediction,
            "Confidence (%)": round(confidence, 2),
            "Pipe Size (mm)": pipe_size,
            "Thickness Loss (mm)": thickness_loss,
            "Material Loss (%)": material_loss,
            "Corrosion (%)": corrosion,
            "Material": material,
            "Grade": grade,
        }
    )

    st.subheader("Prediction Result")

    display_condition_result(prediction)

    st.metric(
        "Model Confidence",
        f"{confidence:.2f}%"
    )

    st.progress(min(confidence / 100, 1.0))

    st.subheader("Class Probabilities")

    p1, p2, p3 = st.columns(3)

    with p1:
        st.metric("Critical", f"{probabilities.get('Critical', 0):.2f}%")

    with p2:
        st.metric("Moderate", f"{probabilities.get('Moderate', 0):.2f}%")

    with p3:
        st.metric("Normal", f"{probabilities.get('Normal', 0):.2f}%")

    display_recommendation(prediction)

    st.subheader("Inspection Summary")
    st.json(input_data)