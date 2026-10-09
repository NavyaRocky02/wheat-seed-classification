
import streamlit as st
import pandas as pd
import joblib
from pathlib import Path

# --------------------------------------------------
# 1. Page Configuration
# --------------------------------------------------
st.set_page_config(
    page_title="Wheat Seed Classification",
    page_icon="🌾",
    layout="centered"
)

# --------------------------------------------------
# 2. Model Path
# --------------------------------------------------
MODEL_PATH = (
    Path(__file__).parent / "improved_wheat_seed_model.pkl"
)

# --------------------------------------------------
# 3. Page Header
# --------------------------------------------------
st.title("🌾 Wheat Seed Classification")

st.write(
    "Enter the physical measurements of a wheat seed "
    "to predict its variety using a trained Random Forest model."
)

st.info(
    "This model classifies wheat seeds into three varieties."
)

# --------------------------------------------------
# 4. Load Trained Model
# --------------------------------------------------
@st.cache_resource
def load_model(model_path, modified_time):
    return joblib.load(model_path)


if not MODEL_PATH.exists():
    st.error(
        "Model file not found! Place "
        "'improved_wheat_seed_model.pkl' in the same "
        "folder as app.py."
    )
    st.stop()

try:
    model = load_model(
        str(MODEL_PATH),
        MODEL_PATH.stat().st_mtime
    )
except Exception as error:
    st.error(f"Unable to load the trained model: {error}")
    st.stop()

# --------------------------------------------------
# 5. Variety Labels
# --------------------------------------------------
# Standard label mapping for the original UCI Seeds dataset.
# Confirm that your notebook uses the same mapping.
variety_names = {
    1: "Kama",
    2: "Rosa",
    3: "Canadian"
}

# --------------------------------------------------
# 6. Input Form
# --------------------------------------------------
st.divider()
st.subheader("Enter Seed Measurements")

with st.form("seed_prediction_form"):

    area = st.number_input(
        "Area",
        min_value=0.0,
        value=15.2,
        step=0.1,
        format="%.3f"
    )

    perimeter = st.number_input(
        "Perimeter",
        min_value=0.0,
        value=14.1,
        step=0.1,
        format="%.3f"
    )

    compactness = st.number_input(
        "Compactness",
        min_value=0.0,
        max_value=1.0,
        value=0.880,
        step=0.001,
        format="%.4f"
    )

    kernel_length = st.number_input(
        "Kernel Length",
        min_value=0.0,
        value=5.5,
        step=0.1,
        format="%.3f"
    )

    kernel_width = st.number_input(
        "Kernel Width",
        min_value=0.0,
        value=3.2,
        step=0.1,
        format="%.3f"
    )

    asymmetry = st.number_input(
        "Asymmetry Coefficient",
        min_value=0.0,
        value=2.1,
        step=0.1,
        format="%.3f"
    )

    groove_length = st.number_input(
        "Kernel Groove Length",
        min_value=0.0,
        value=5.0,
        step=0.1,
        format="%.3f"
    )

    submitted = st.form_submit_button(
        "🔍 Predict Variety",
        use_container_width=True
    )

# --------------------------------------------------
# 7. Prediction
# --------------------------------------------------
if submitted:

    # Keep the feature names and order identical
    # to those used when training the model.
    input_data = pd.DataFrame(
        [[
            area,
            perimeter,
            compactness,
            kernel_length,
            kernel_width,
            asymmetry,
            groove_length
        ]],
        columns=[
            "area",
            "perimeter",
            "compactness",
            "kernel_length",
            "kernel_width",
            "asymmetry_coefficient",
            "kernel_groove_length"
        ]
    )

    try:
        prediction = model.predict(input_data)[0]

        predicted_name = variety_names.get(
            int(prediction),
            f"Unknown (label {prediction})"
        )

        st.success(
            f"Predicted Wheat Seed Variety: {predicted_name}"
        )

        st.write(f"**Predicted label:** {prediction}")

        # Display confidence when supported by the model.
        if hasattr(model, "predict_proba"):
            probabilities = model.predict_proba(input_data)[0]

            st.subheader("Prediction Probabilities")

            probability_data = pd.DataFrame({
                "Variety": [
                    variety_names.get(int(label), str(label))
                    for label in model.classes_
                ],
                "Probability": probabilities
            })

            st.bar_chart(
                probability_data.set_index("Variety")
            )

            st.caption(
                "Probabilities represent the model's estimates, "
                "not guaranteed real-world accuracy."
            )

        st.caption(
            "Prediction generated by your trained "
            "Random Forest model."
        )

    except Exception as error:
        st.error(f"Prediction failed: {error}")

# --------------------------------------------------
# 8. Footer
# --------------------------------------------------
st.divider()

st.caption(
    "Machine Learning Project | Wheat Seed Classification"
)
