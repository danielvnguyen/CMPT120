import turtle
from functions import drawBar, getProcessedData, calculateError
from sklearn.linear_model import LinearRegression

# Ask user for the file name of the data they'd like to use
# Then open the file and convert it to a list
fileName = input("What is the file name of data set?\n")
dataFile = open(fileName)
dataFile.readline() # Skips header row 
dataFile = list(dataFile)

# Ask the user which column is the output
outputColumn = int(input("Which column are the output values in?\n"))

# Ask the user which column(s) are the input
inputColumns = input("Which column(s) are the input values in? (Comma seperated)\n")
inputColumns = inputColumns.split(",")

for i in range(len(inputColumns)):
  inputColumns[i] = int(inputColumns[i])

# Processing the data for the machine
processedData = getProcessedData(dataFile, outputColumn, inputColumns)
userDataOutput = processedData[0]
userDataInput = processedData[1]

# Setting the training data as 80% of the total data
training_input = userDataInput[0:len(userDataInput)*80//100]
training_output = userDataOutput[0:len(userDataOutput)*80//100]

# Setting the testing data as 20% of the total data
test_input = userDataInput[len(userDataInput)*80//100:]
test_output = userDataOutput[len(userDataOutput)*80//100:]

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
window.bgcolor("lightyellow")
window.screensize(750, 400)

# Getting the highest number to scale the graph.
highest_number = max(percentile.values())

# Draw a bar for each total number within 'percentile.'
for key in percentile.keys():
  total_number = percentile[key]
  drawBar(total_number, key, highest_number)
