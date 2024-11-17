import pickle
import pandas as pd

# Load the test data
test_data = pd.read_csv('../data/test_data.csv')

# Load the model
try:
    with open('../models/linear_regression_model.pkl', 'rb') as f:
        model = pickle.load(f)
except FileNotFoundError:
    print("Model file not found!")
    exit()

# Dummy prediction logic
for index, row in test_data.iterrows():
    square_feet = row['square_feet']
    price = row['price']
    print(f"Predicted price for {square_feet} square feet: {price}")
