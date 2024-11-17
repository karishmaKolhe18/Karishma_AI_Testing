import pickle
import pandas as pd

# Update paths to use repository root-relative paths
test_data_path = 'data/test_data.csv'
model_path = 'models/linear_regression_model.pkl'

# Load the test data
try:
    test_data = pd.read_csv(test_data_path)
except FileNotFoundError:
    print(f"Test data file not found: {test_data_path}")
    exit()

# Load the model
try:
    with open(model_path, 'rb') as f:
        model = pickle.load(f)
except FileNotFoundError:
    print(f"Model file not found: {model_path}")
    exit()

# Dummy prediction logic
for index, row in test_data.iterrows():
    square_feet = row['square_feet']
    price = row['price']
    print(f"Predicted price for {square_feet} square feet: {price}")
