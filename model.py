# Importing the necessary libraries

import pandas as pd
from sklearn.model_selection import train_test_split
from xgboost import XGBRegressor
import joblib

# Load the dataset
calories_df = pd.read_csv("datasets/calories.csv")
exercise_df = pd.read_csv("datasets/exercise.csv")

# Combining the Two DataFrames
df = pd.concat(
    [exercise_df, calories_df["Calories"]], 
    axis=1
)

# Converting the test data to numerical values
df.replace(
    {"Gender": {'male': 0, 'female': 1}}, 
    inplace=True
)

# Features and Target
X = df.drop(columns=['User_ID', 'Calories'], axis=1)
Y = df['Calories']

# Splitting the dataset into training and testing sets
X_train, X_test, Y_train, Y_test = train_test_split(
    X, Y, test_size=0.2, random_state=2
)

# XGBoost Regressor Model:
model = XGBRegressor()

# Training the model
model.fit(X_train, Y_train)

joblib.dump(model, "model.pkl")
print("✅ Model saved successfully as xgb_regressor_model.pkl")