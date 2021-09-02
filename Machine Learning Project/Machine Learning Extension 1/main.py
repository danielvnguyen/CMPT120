# Description: After processing a data file, this program sends
# 80% of the data for the machine to analyze. The program then sends 
# the remaining 20% of the data for the machine to predict the outcome for.
# A bar graph is then displayed to represent the accuracy of the predictions.

import turtle
from functions import drawBar, getProcessedData, calculateError
from sklearn.linear_model import LinearRegression

# Processing the data for the machine
processedData = getProcessedData()
areaBurned = processedData[0]
dailyData = processedData[1]


# Setting the training data as 80% of the total data
training_input = dailyData[0:len(dailyData)*80//100]
training_output = areaBurned[0:len(areaBurned)*80//100]

# Setting the testing data as 20% of the total data
test_input = dailyData[len(dailyData)*80//100:]
test_output = areaBurned[len(areaBurned)*80//100:]

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
window.bgcolor("lightgreen")
window.screensize(750, 400)

# Draw a bar for each total number within 'percentile.'
for key in percentile.keys():
  total_number = percentile[key]
  drawBar(total_number, key)
