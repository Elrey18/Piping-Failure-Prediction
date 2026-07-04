from pathlib import Path
import joblib
import pandas as pd


# ==========================
# Load saved objects
# ==========================

BASE_DIR = Path(__file__).resolve().parents[1]
MODEL_DIR = BASE_DIR / "models"

model = joblib.load(MODEL_DIR / "random_forest.pkl")
scaler = joblib.load(MODEL_DIR / "scaler.pkl")
label_encoder = joblib.load(MODEL_DIR / "label_encoder.pkl")
feature_columns = joblib.load(MODEL_DIR / "feature_columns.pkl")


# Numerical columns only
NUMERIC_COLUMNS = [
    "Pipe_Size_mm",
    "Thickness_mm",
    "Max_Pressure_psi",
    "Temperature_C",
    "Corrosion_Impact_Percent",
    "Thickness_Loss_mm",
    "Material_Loss_Percent",
    "Time_Years",
]


def predict_pipeline(input_data):
    """
    Predict pipeline condition from user inspection data.

    Returns:
        prediction_label: str
        confidence: float
        probability_dict: dict
    """

    # Start with all expected model columns set to zero
    model_input = {col: 0.0 for col in feature_columns}

    # Fill numerical values
    for col in NUMERIC_COLUMNS:
        if col in input_data:
            model_input[col] = float(input_data[col])

    # Handle raw Material input
    material = input_data.get("Material")

    if material == "Fiberglass":
        model_input["Material_Fiberglass"] = 1.0

    elif material == "HDPE":
        model_input["Material_HDPE"] = 1.0

    elif material == "PVC":
        model_input["Material_PVC"] = 1.0

    elif material == "Stainless Steel":
        model_input["Material_Stainless Steel"] = 1.0

    # Carbon Steel is the baseline category, so all material dummy columns remain 0

    # Handle raw Grade input
    grade = input_data.get("Grade")

    if grade == "API 5L X52":
        model_input["Grade_API 5L X52"] = 1.0

    elif grade == "API 5L X65":
        model_input["Grade_API 5L X65"] = 1.0

    elif grade == "ASTM A106 Grade B":
        model_input["Grade_ASTM A106 Grade B"] = 1.0

    elif grade == "ASTM A333 Grade 6":
        model_input["Grade_ASTM A333 Grade 6"] = 1.0

    # API 5L X42 is the baseline category, so all grade dummy columns remain 0

    # Create DataFrame in exact training order
    df = pd.DataFrame([model_input])
    df = df.reindex(columns=feature_columns, fill_value=0.0)

    # Scale ONLY numerical columns
    df_scaled = df.copy()
    df_scaled[NUMERIC_COLUMNS] = scaler.transform(df[NUMERIC_COLUMNS])

    # Predict
    prediction_encoded = model.predict(df_scaled)[0]
    probabilities = model.predict_proba(df_scaled)[0]

    # Decode prediction label
    prediction_label = label_encoder.inverse_transform([prediction_encoded])[0]

    # Probability dictionary
    probability_dict = {
        label: float(prob * 100)
        for label, prob in zip(label_encoder.classes_, probabilities)
    }

    confidence = max(probability_dict.values())

    return prediction_label, confidence, probability_dict