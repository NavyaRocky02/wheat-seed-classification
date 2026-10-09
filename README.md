# 🌾 Wheat Seed Classification Using Machine Learning

## 📌 Project Overview
This project uses machine learning to classify wheat seeds into three varieties: Kama, Rosa, and Canadian, based on their physical measurements. A Streamlit web application allows users to enter seed measurements and receive a predicted variety.

## 🎯 Objectives
- Explore and analyze the wheat seed dataset.
- Train and evaluate multiple machine learning models.
- Improve model performance using cross-validation and hyperparameter tuning.
- Build an interactive web application for predictions.

## 📊 Dataset
The dataset contains 210 samples, with seven input features and one target label.

**Features:**
- Area
- Perimeter
- Compactness
- Kernel Length
- Kernel Width
- Asymmetry Coefficient
- Kernel Groove Length

**Target:** Wheat seed variety (1, 2, or 3).

## 🤖 Machine Learning Models
- K-Nearest Neighbors (KNN)
- Decision Tree
- Random Forest

The improved notebook uses stratified cross-validation and GridSearchCV for model tuning.

## 🛠️ Technologies Used
- Python
- Pandas and NumPy
- Scikit-learn
- Matplotlib
- Jupyter Notebook
- Streamlit
- Joblib

## 🚀 Run the Project Locally

1. Clone this repository:

   ```bash
   git clone https://github.com/NavyaRocky02/wheat-seed-classification.git
   cd wheat-seed-classification
   ```

2. Install the required packages:

   ```bash
   pip install streamlit pandas scikit-learn joblib
   ```

3. Make sure `improved_wheat_seed_model.pkl` is in the same folder as `app.py`.

4. Start the application:

   ```bash
   streamlit run app.py
   ```

5. Open the local URL displayed in the terminal.

## 📁 Project Files
- `01_Wheat_Seed_Classification.ipynb` — Initial model development.
- `02_Improved_Wheat_Seed_Classification.ipynb` — Model evaluation and tuning.
- `app.py` — Streamlit application.
- `seeds.csv` — Dataset.
- `improved_wheat_seed_model.pkl` — Trained model required by the application.

## 👩‍💻 Future Improvements
- Add model performance visualizations.
- Improve input validation and user experience.
- Deploy the application online.

## 📄 License
This project is available for educational and learning purposes.
