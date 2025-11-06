# Importing the necessary libraries

import pandas as pd
from sklearn.model_selection import train_test_split
from xgboost import XGBRegressor
from sklearn.metrics import mean_squared_error

# Load the dataset
calories_df = pd.read_csv("datasets/calories.csv")
exercise_df = pd.read_csv("datasets/exercise.csv")