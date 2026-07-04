import streamlit as st


def render_sidebar():
    """
    Render consistent sidebar navigation across all pages.
    """

    st.sidebar.title("🛢️ Pipeline Integrity AI")
    st.sidebar.markdown("---")

    st.sidebar.success("System Status: Online")

    st.sidebar.markdown("### Navigation")

    st.sidebar.page_link("app.py", label="Home", icon="🏠")
    st.sidebar.page_link("pages/1_Inspection.py", label="Inspection", icon="🔍")
    st.sidebar.page_link("pages/2_Dashboard.py", label="Dashboard", icon="📊")
    st.sidebar.page_link("pages/3_Reports.py", label="Reports", icon="📄")
    st.sidebar.page_link("pages/4_About.py", label="About", icon="ℹ️")

    st.sidebar.markdown("---")
    st.sidebar.caption("Version 2.0")


def display_condition_result(prediction):
    """
    Display prediction result with color-coded formatting.
    """

    if prediction == "Normal":
        st.success(f"🟢 Pipeline Condition: {prediction}")

    elif prediction == "Moderate":
        st.warning(f"🟡 Pipeline Condition: {prediction}")

    else:
        st.error(f"🔴 Pipeline Condition: {prediction}")


def display_recommendation(prediction):
    """
    Display engineering recommendation based on prediction.
    """

    st.subheader("Maintenance Recommendation")

    if prediction == "Normal":
        st.success("""
✅ Continue normal operation.

• Routine inspection only  
• No immediate maintenance required  
• Monitor periodically  
""")

    elif prediction == "Moderate":
        st.warning("""
⚠ Schedule maintenance soon.

• Increase inspection frequency  
• Monitor corrosion and material loss  
• Plan preventive maintenance  
""")

    else:
        st.error("""
🚨 Immediate action required.

• Inspect pipeline immediately  
• Repair or replace damaged section  
• Consider reducing or suspending operation  
• Perform full integrity assessment  
""")

def apply_custom_style():
    """
    Apply custom CSS styling across the Streamlit app.
    """

    st.markdown(
        """
        <style>
        /* Main page background */
        .stApp {
            background-color: #f7f9fc;
        }

        /* Sidebar */
        section[data-testid="stSidebar"] {
            background-color: #eef3f8;
        }

        /* Headings */
        h1, h2, h3 {
            color: #1f2d3d;
        }

        /* Metric cards */
        div[data-testid="stMetric"] {
            background-color: #ffffff;
            padding: 18px;
            border-radius: 12px;
            border: 1px solid #e6e9ef;
            box-shadow: 0px 2px 8px rgba(0,0,0,0.04);
        }

        /* Buttons */
        .stButton > button {
            background-color: #0f4c81;
            color: white;
            border-radius: 10px;
            border: none;
            padding: 0.7rem 1.2rem;
            font-weight: 600;
        }

        .stButton > button:hover {
            background-color: #0b3a63;
            color: white;
        }

        /* Info blocks */
        .stAlert {
            border-radius: 10px;
        }

        /* Dataframe */
        div[data-testid="stDataFrame"] {
            border-radius: 10px;
        }

        /* Footer text */
        .footer {
            text-align: center;
            color: #6c757d;
            font-size: 14px;
            margin-top: 40px;
        }
        </style>
        """,
        unsafe_allow_html=True
    )