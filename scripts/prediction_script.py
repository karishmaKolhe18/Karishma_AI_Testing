import pickle
import pandas as pd

# Update paths to use repository root-relative paths
test_data_path = 'data/test_inputs.csv'
model_path = 'models/linear_regression_model.pkl'

# Load the model
try:
    with open(model_path, 'rb') as f:
        model = pickle.load(f)
except FileNotFoundError:
    print(f"Model file not found: {model_path}")
    exit()

# Load test inputs
try:
    test_data = pd.read_csv(test_data_path)
    for index, row in test_data.iterrows():
        square_feet = row['square_feet']
        predicted_price = model.predict([[square_feet]])
        print(f"Predicted price for {square_feet} square feet: {predicted_price[0]:.2f}")
except Exception as e:
    print(f"An error occurred: {e}")
