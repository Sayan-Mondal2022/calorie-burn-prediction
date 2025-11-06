# Importing the necessary libraries

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import BaggingRegressor
from sklearn.tree import DecisionTreeRegressor
import joblib

# Load the dataset
calories_df = pd.read_csv("datasets/calories.csv")
exercise_df = pd.read_csv("datasets/exercise.csv")

# Combining the Two DataFrames
df = pd.concat(
    [exercise_df, calories_df["Calories"]], 
    axis=1
)
print("✅ DataFrames combined successfully\n")

# Converting the test data to numerical values
df.replace(
    {"Gender": {'male': 0, 'female': 1}}, 
    inplace=True
)
print("✅ Categorical values converted to numerical successfully\n")

# Features and Target
X = df.drop(columns=['User_ID', 'Calories'], axis=1)
Y = df['Calories']

# Splitting the dataset into training and testing sets
X_train, X_test, Y_train, Y_test = train_test_split(
    X, Y, test_size=0.2, random_state=2
)
print("✅ Dataset split into training and testing sets successfully\n")

# Bagging Regressor with Decision Tree
model = BaggingRegressor(
    estimator=DecisionTreeRegressor(max_depth=8),
    n_estimators=100,
    random_state=42,
    bootstrap=True
)

# Training the model
model.fit(X_train, Y_train)
print("✅ Model trained successfully\n")

# Saving the trained model
joblib.dump(model, "model.pkl")
print("✅ Model saved successfully as xgb_regressor_model.pkl")