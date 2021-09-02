# Description: Trains a program to find the co-efficients
# of the functions y = c1x1 + c2x2 + c3x3
# c = co-efficient, x = input

# Gets the output and input functions from functions.py
from functions import createInput, createOutput
# Gets the machine learning model
from sklearn.linear_model import LinearRegression

# Creating the training data
values = createInput(100)
resultingValues = createOutput(values);

# Training the model
predictor = LinearRegression(n_jobs = -1)
predictor.fit(X=values, y=resultingValues)

# Testing the model
X_test = [[10,20,30]]
outcome = predictor.predict(X=X_test)
coefficients = predictor.coef_

# Outcome of testing the model
print("Prediction: "+ str(outcome))
print("Coefficients: " + str(coefficients))
