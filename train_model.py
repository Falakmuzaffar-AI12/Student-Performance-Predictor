import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score

import joblib

# Load dataset
data = pd.read_csv("dataset/student_performance.csv")

# Display dataset information
print("Dataset loaded successfully!")
print(data.head())
print(data.info())
# Input features
X = data[["math score", "reading score"]]

# Target variable
y = data["writing score"]
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)
# Create Linear Regression model
model = LinearRegression()

# Train the model
model.fit(X_train, y_train)

print("Model trained successfully!")
# Make predictions
predictions = model.predict(X_test)

# Evaluate performance
mae = mean_absolute_error(y_test, predictions)
r2 = r2_score(y_test, predictions)

print("Mean Absolute Error:", mae)
print("R2 Score:", r2)
# Save trained model
joblib.dump(model, "model.pkl")

print("Model saved successfully!")