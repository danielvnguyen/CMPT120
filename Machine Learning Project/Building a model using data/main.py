# Description: This program lets the machine analyzes a large 
# percentage of a data file in order to predict the outcome for the 
# remaining percentage of the data file. The program then produces a 
# bar graph to display the accuracy of the predictions.

import turtle
from functions import drawBar, getProcessedData, calculateError
from sklearn.linear_model import LinearRegression

# Processing the data for the machine
processedData = getProcessedData()
bikesRented = processedData[0]
dailyData = processedData[1]

# Setting the training data as 80% of the total data
training_output = bikesRented[0:len(bikesRented)*80//100]
training_input = dailyData[0:len(dailyData)*80//100]

# Setting the testing data as 20% of the total data
test_output = bikesRented[len(bikesRented)*80//100:]
test_input = dailyData[len(dailyData)*80//100:]

# Training the Model:
predictor = LinearRegression(n_jobs=-1)
predictor.fit(X=training_input, y=training_output)

# Testing the model
X_test = test_input
outcome = predictor.predict(X=X_test)

# Creating a list of the total values of percentage errors in specific ranges.
percentile = calculateError(test_output, outcome)

# Setting up the window for the turtle chart
window = turtle.Screen()
window.bgcolor("lightblue")
window.screensize(900, 400)

# Draw a bar for each total number within 'percentile.'
for key in percentile.keys():
  total_number = percentile[key]
  drawBar(total_number, key)
