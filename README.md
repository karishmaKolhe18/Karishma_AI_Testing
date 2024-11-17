# AI Testing Project

This project demonstrates a basic setup for integrating AI testing tools into a CI/CD pipeline.

## File Structure
- **data/**: Contains test datasets.
- **models/**: Pre-trained Linear Regression model (dummy).
- **scripts/**: Scripts for predictions and testing.

## Usage
1. Place your actual model file in the `models/` folder.
2. Run `scripts/prediction_script.py` to make predictions based on `data/test_data.csv`.

## CI/CD Pipeline
A GitHub Actions workflow is included to automate testing and deployment.
