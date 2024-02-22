# Import necessary libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.metrics import mean_squared_error, r2_score

# Load your dataset (replace 'your_dataset.csv' with your actual dataset)
data = pd.read_csv('your_dataset.csv')

# Simple Linear Regression (SLR)

# Choose independent (X) and dependent (y) variables
X_slr = data['independent_variable'].values.reshape(-1, 1)
y_slr = data['dependent_variable'].values

# Split the data into training and testing sets
X_train_slr, X_test_slr, y_train_slr, y_test_slr = train_test_split(X_slr, y_slr, test_size=0.2, random_state=42)

# Create and train the SLR model
slr_model = LinearRegression()
slr_model.fit(X_train_slr, y_train_slr)

# Make predictions
y_pred_slr = slr_model.predict(X_test_slr)

# Evaluate SLR model
mse_slr = mean_squared_error(y_test_slr, y_pred_slr)
r2_slr = r2_score(y_test_slr, y_pred_slr)

# Multiple Linear Regression (MLR)

# Choose multiple independent variables and the dependent variable
X_mlr = data[['independent_var1', 'independent_var2', 'independent_var3']]
y_mlr = data['dependent_variable'].values

# Split the data into training and testing sets
X_train_mlr, X_test_mlr, y_train_mlr, y_test_mlr = train_test_split(X_mlr, y_mlr, test_size=0.2, random_state=42)

# Create and train the MLR model
mlr_model = LinearRegression()
mlr_model.fit(X_train_mlr, y_train_mlr)

# Make predictions
y_pred_mlr = mlr_model.predict(X_test_mlr)

# Evaluate MLR model
mse_mlr = mean_squared_error(y_test_mlr, y_pred_mlr)
r2_mlr = r2_score(y_test_mlr, y_pred_mlr)

# Polynomial Regression

# Choose independent and dependent variables
X_poly = data['independent_variable'].values.reshape(-1, 1)
y_poly = data['dependent_variable'].values

# Transform features to polynomial degree (e.g., degree=2)
poly = PolynomialFeatures(degree=2)
X_poly_transformed = poly.fit_transform(X_poly)

# Split the data into training and testing sets
X_train_poly, X_test_poly, y_train_poly, y_test_poly = train_test_split(X_poly_transformed, y_poly, test_size=0.2, random_state=42)

# Create and train the Polynomial Regression model
poly_model = LinearRegression()
poly_model.fit(X_train_poly, y_train_poly)

# Make predictions
y_pred_poly = poly_model.predict(X_test_poly)

# Evaluate Polynomial Regression model
mse_poly = mean_squared_error(y_test_poly, y_pred_poly)
r2_poly = r2_score(y_test_poly, y_pred_poly)
