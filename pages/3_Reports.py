import streamlit as st
from src.report_generator import generate_pdf_report
from src.utils import render_sidebar, apply_custom_style


st.set_page_config(
    page_title="Reports",
    page_icon="📄",
    layout="wide",
    initial_sidebar_state="expanded"
)

apply_custom_style()
render_sidebar()


st.title("📄 Engineering Inspection Report")

st.write(
    "Generate a downloadable PDF report from the latest pipeline inspection prediction."
)

st.divider()


last_prediction = st.session_state.get("last_prediction", None)

if last_prediction is None:

    st.warning(
        "No inspection prediction found yet. Please go to the Inspection page and run a prediction first."
    )

else:

    prediction = last_prediction["prediction"]
    confidence = last_prediction["confidence"]
    probabilities = last_prediction["probabilities"]
    input_data = last_prediction["input_data"]

    st.subheader("Latest Prediction Summary")

    c1, c2, c3 = st.columns(3)

    with c1:
        st.metric("Predicted Condition", prediction)

    with c2:
        st.metric("Model Confidence", f"{confidence:.2f}%")

    with c3:
        st.metric("Model", "Random Forest")

    st.divider()

    st.subheader("Inspection Data")
    st.json(input_data)

    st.divider()

    st.subheader("Class Probabilities")

    p1, p2, p3 = st.columns(3)

    with p1:
        st.metric("Critical", f"{probabilities.get('Critical', 0):.2f}%")

    with p2:
        st.metric("Moderate", f"{probabilities.get('Moderate', 0):.2f}%")

    with p3:
        st.metric("Normal", f"{probabilities.get('Normal', 0):.2f}%")

    st.divider()

    st.subheader("Generate Report")

    if st.button("Generate PDF Report", use_container_width=True):

        pdf_bytes, filename = generate_pdf_report(last_prediction)

        st.success("PDF report generated successfully.")

        st.download_button(
            label="Download Inspection Report",
            data=pdf_bytes,
            file_name=filename,
            mime="application/pdf",
            use_container_width=True
        )