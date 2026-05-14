# Program 1: Linear Regression on California Housing Dataset
from sklearn.datasets import fetch_california_housing
# from sklearn.model_selection import train_test_split
# from sklearn.preprocessing import StandardScaler
# from sklearn.linear_model import LinearRegression
# from sklearn.metrics import mean_squared_error, r2_score
# import matplotlib.pyplot as plt
# import numpy as np
# Load dataset
data = fetch_california_housing()
X = data.data
y = data.target
print("Feature matrix shape :", X.shape)
# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)
# Feature scaling
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)
# Train model
model = LinearRegression()
model.fit(X_train, y_train)
# Predictions
y_pred_train = model.predict(X_train)
y_pred_test = model.predict(X_test)
# Metrics
train_mse = mean_squared_error(y_train, y_pred_train)
test_mse = mean_squared_error(y_test, y_pred_test)
rmse = np.sqrt(test_mse)
r2 = r2_score(y_test, y_pred_test)
print("Training MSE :", train_mse)
print("Testing MSE :", test_mse)
print("Testing RMSE :", rmse)
print("Testing R2 :", r2)
# Plot
plt.scatter(y_test, y_pred_test)
plt.xlabel("Actual Values")
plt.ylabel("Predicted Values")
plt.title("Actual vs Predicted")
plt.show()