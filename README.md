# 🔥 Calorie Burn Prediction using Machine Learning

Predict the number of calories burned during physical activity using advanced regression models.  
This project combines **data science**, **machine learning**, and **streamlit deployment** to estimate calorie expenditure with **high accuracy**.


## 📖 Project Overview
The **Calorie Burn Prediction** project aims to accurately estimate calories burned during physical activity using measurable human attributes such as **age, gender, height, weight, heart rate**, and **duration**.  
It’s designed to help users and fitness enthusiasts understand their calorie expenditure and optimize workouts or diets accordingly.


## 🎥 Demo

### 🖼️ Web App Interface
<img width="1302" height="854" alt="App Screenshot" src="https://github.com/user-attachments/assets/19c7008a-185f-40a9-846f-f7a4ad4ff385" />

### 🚀 Live Demo  
**[🎥 Try the App Here](https://sayan-mondal2022-calorie-burn-prediction-app-htorh9.streamlit.app/)**  

*(Hosted on Streamlit Cloud — runs the trained model for real-time calorie predictions)*

---

## 🧠 Technologies Used
- **Python 3.x**
- **Pandas**, **NumPy** – Data processing  
- **Matplotlib**, **Seaborn** – Data visualization  
- **Scikit-learn** – Model training and evaluation  
- **Streamlit** – Web app deployment  
- **Jupyter Notebook** – Model development  


## 📊 Dataset
The dataset includes physiological and exercise-related features:

| Feature | Description |
|----------|--------------|
| Gender | Male/Female |
| Age | Person’s age (years) |
| Height | Height in centimeters |
| Weight | Weight in kilograms |
| Duration | Duration of activity (minutes) |
| Heart Rate | Heart beats per minute |
| Body Temperature | Body temperature during activity |
| Calories | Target variable (calories burned) |

> Data preprocessing included encoding categorical data, handling missing values, and normalization for numerical stability.


## ⚙️ Project Workflow
1. **Data Collection** – Import and merge multiple CSV datasets  
2. **Preprocessing** – Encoding, normalization, and cleaning  
3. **EDA (Exploratory Data Analysis)** – Correlation plots and visual insights  
4. **Feature Selection** – Identify key contributors to calorie burn  
5. **Model Training** – Train regression models (Linear, Random Forest, XGBoost)  
6. **Model Evaluation** – Compare models and tune hyperparameters  
7. **Deployment** – Build Streamlit app for interactive predictions  


## 📈 Model Evaluation Metrics

| Metric | Value |
|:--|:--:|
| **Mean Absolute Error (MAE)** | 3.23 |
| **Mean Squared Error (MSE)** | 21.49 |
| **Root Mean Squared Error (RMSE)** | 4.64 |
| **R² Score** | **0.9945 ✅** |

📊 **Interpretation:**  
An **R² of 0.9945** signifies excellent predictive performance, meaning the model explains over **99% of the variance** in calorie burn outcomes.


## 🏆 Results
- Achieved **R² = 0.9945** with extremely low error metrics.  
- Key features affecting calorie burn: **Heart Rate**, **Duration**, and **Body Temperature**.  
- Integrated with **Streamlit** for user-friendly, interactive predictions.  


## 💻 Installation & Usage

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/Sayan-Mondal2022/calorie-burn-prediction.git
cd calorie-burn-prediction
```

### 2️⃣ Create the Virtual Environment and activate the .venv
```bash
python -m venv .venv

# TO activate the .venv
source .venv/Scripts/activate
```

### 3️⃣ Install Required Packages
```bash
pip install -r requirements.txt
```

### 4️⃣ Run the Streamlit App
```bash
streamlit run app.py
```

## 📂 Project Structure

```bash
calorie-burn-prediction/
├── datasets/
│   ├── calories.csv
│   ├── exercise.csv
├── model.ipynb
├── model.pkl
├── app.py
├── requirements.txt
└── README.md
```

## 🙏 Acknowledgement

I would like to acknowledge the open-source tools and technologies that made this project possible.  
This project was developed using a powerful Python ecosystem including:

- **Pandas** and **NumPy** for efficient data handling  
- **Matplotlib** and **Seaborn** for insightful data visualization  
- **Scikit-learn** for robust model building and evaluation  
- **Streamlit** for deploying an interactive web application  

I also extend my gratitude to the creators and providers of the **Calorie and Exercise dataset**, which served as the foundation for model training and evaluation.

⭐ *Thank you for taking the time to explore my project! If you found it helpful, please consider giving it a star on GitHub — it truly motivates me to create more!* 🚀
