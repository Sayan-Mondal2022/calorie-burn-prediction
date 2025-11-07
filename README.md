# Calorie Burn Prediction  

The **Calorie Burn Prediction** project is a machine learning-based application designed to estimate the number of calories burned during physical activities using user-provided data such as duration, heart rate, age, gender, and body metrics. The model is built using the **XGBoost Regressor**, a powerful gradient boosting algorithm known for its high performance and accuracy in regression tasks.  

The project involves data preprocessing, feature selection, model training, and evaluation to ensure reliable predictions. The trained model can help users monitor their daily energy expenditure, optimize workout plans, and maintain a healthy lifestyle. The system is further integrated into an interactive interface, allowing users to input their activity data and instantly receive calorie burn predictions.  

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

