# Heart Disease Prediction

This project predicts heart disease using a machine learning model trained on a dataset of patient medical information.

## Features:
- **Preprocessed Dataset**: The `heart.csv` dataset is cleaned and processed for training.
- **Feature Selection**: Important features are selected based on Mutual Information and Feature Importance.
- **Trained Model**: The final model is a **Random Forest Classifier**.
- **Web Application**: A **Streamlit-based web app** allows users to enter patient details and receive predictions.

## Installation

Clone this repository and install the required dependencies:

```bash
git clone https://github.com/your-username/Heart-Disease-Prediction.git
cd Heart-Disease-Prediction
pip install -r requirements.txt
```

## Running the Streamlit App

To launch the Streamlit web app:

```bash
streamlit run app.py
```

## Running the Flask App

Alternatively, if using Flask:

```bash
python app.py
```

## Dataset

The dataset used for training is `heart.csv`, which contains the following features:

- **Age**, **Sex**, **Resting Blood Pressure**, **Cholesterol Level**
- **Maximum Heart Rate**, **Oldpeak (ST Depression)**
- **Exercise-Induced Angina**, **ST Slope**, **Chest Pain Type**, **Resting ECG**

## Model Training

- **Model Used**: Random Forest Classifier  
- **Feature Selection**: Based on Feature Importance  
- **Hyperparameter Tuning**: Performed using GridSearchCV  
- **Performance Metrics**:
  - **Accuracy**: 84.4%
  - **F1-Score**: 83.8%

## Results & Confusion Matrix

The confusion matrix for the best-performing model:

| Actual \ Predicted | No Disease | Disease |
|--------------------|-----------|---------|
| **No Disease**    | 61        | 15      |
| **Disease**       | 9         | 56      |

## Contributors

- **Omkar Santosh Kandalkar**

---

## License

This project is for educational purposes only.
