# Calorie Burn Prediction  

This project predicts the number of calories burned during exercise using a machine learning model. It employs a `Bagging Regressor` trained on user biometrics (`age, height, weight, gender`) and workout data (`duration, heart rate`).
The model provides real-time, on-demand calorie predictions through an interactive web application. It helps users monitor and understand their fitness performance more effectively.

<img width="1302" height="854" alt="image" src="https://github.com/user-attachments/assets/19c7008a-185f-40a9-846f-f7a4ad4ff385" />

**[🎥 Demo Link](https://sayan-mondal2022-calorie-burn-prediction-app-htorh9.streamlit.app/)**  

---

## 🛠 Tech Stack

### Programming & Core ML:

1. Python - Primary programming language
2. Scikit-learn - Machine learning library
3. BaggingRegressor - Ensemble model with 100 estimators
4. DecisionTreeRegressor - Base learner (max_depth=8)
5. Pandas - Data manipulation and preprocessing
6. Joblib - Model serialization and storage
7. Streamlit - Interactive web application framework

### Machine Learning Architecture:

1. Ensemble Method: Bagging (Bootstrap Aggregating)
2. Base Algorithm: Decision Tree Regressor

- Model Type: Supervised Learning - Regression
- Training Approach: Parallel training with bootstrap sampling

---

## 🔧 Installation and Usage

To run this project locally, follow these steps:

1. Clone the repository:
```bash
git clone https://github.com/Sayan-Mondal2022/calorie-burn-prediction.git
cd calorie-burn-prediction
```

2. Install the required dependencies:
```bash
pip install -r requirements.txt
```

3. Run the Streamlit app:
```bash
streamlit run app.py
```
This will launch the web application in your browser.

---

## 📁 Repository Structure

```bash
.
├── app.py              # The Streamlit web application
├── model.ipynb         # Jupyter Notebook for model development and evaluation
├── model.py            # Python script to train and save the model
├── model.pkl           # Saved (serialized) machine learning model
├── requirements.txt    # List of Python dependencies
├── datasets/
│   ├── calories.csv    # Target variable data
│   └── exercise.csv    # Feature data
└── README.md           # This README file
```

---

### 🏆 Acknowledgement  

- **[Python](https://www.python.org/):** Used as the primary programming language for implementing the entire project.  
- **[Scikit-learn](https://scikit-learn.org/):** Provided the machine learning framework to build the BaggingRegressor ensemble model with DecisionTreeRegressor as the base learner.  
- **[Pandas](https://pandas.pydata.org/):** Used for efficient data manipulation, cleaning, and preprocessing.  
- **[Joblib](https://joblib.readthedocs.io/):** Enabled fast model serialization and storage for easy reuse.  
- **[Streamlit](https://streamlit.io/):** Used to create an interactive and user-friendly web application interface for model deployment.

