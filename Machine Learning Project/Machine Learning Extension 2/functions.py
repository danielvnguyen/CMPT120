import turtle

def getProcessedData(dataFile, outputColumn, inputColumns):
  '''
  Gets the data from the file in an organized fashion
  Input: datafile - the user given file being used to process the data of 
  outputColumn - the user given column that has the desired output values
  inputColumns - the user given column(s) that has the desired input values
  Output: Tuple of the output values and input values
  '''

  # Output Variable
  outputValues = []
  # Input Variable
  inputValues = []

  for i in range(len(dataFile)):

    # Building input and output lists
    row = dataFile[i]
    outputValues.append((row.split(",")[outputColumn-1])) # Gets output values

    # Keeps track of the inputs values in a specific row
    rowValues = []
    # Iterates through the list of user given columns to build a list of the values at those collumn
    for index in inputColumns:
      rowValues.append(row.split(",")[index-1])

    # Making values in outputValues into floats
    outputValues[i] = float(outputValues[i])
    
    # Goes through all the information in each row's data and converts it to a float
    for n in range(len(rowValues)): 
      rowValues[n] = float(rowValues[n])

    # Adds the data from the list
    inputValues.append(rowValues)
      
  return (outputValues, inputValues)

def calculateError(test_output, outcome):
  '''
  Gives the percent error of the program's predicted data as a dictionary of percentiles
  Input:
  test_output: List of the actual output values
  outcome: List of the predicted output values
  Output: Returns a dictionary of the percentiles of the accuracy of the data
  '''
  # List to keep track of the percentage error
  errorPercentage = []

  # Get the percentage error from the prediction and real value
  for i in range(len(outcome)):
    realValue = test_output[i]
    if realValue != 0:
      predictedValues = outcome[i]
      percentage_error = (abs(realValue - predictedValues))/realValue
      errorPercentage.append(percentage_error)

  # Dictionary to keep track of categories for the error percentage
  percentile = {"<10":0,"<20":0,"<30":0,"<40":0,"<50":0,"<60":0,"<70":0,"<80":0,"<90":0,"<100":0,">100":0}

# Iterates through the list of percent errors
  for percentage in errorPercentage:
    # Always assumed to be greater than 100% error
    percentile[">100"] += 1
    # Iterate through each percentile range to see if the percent fits
    for i in range(1,11):
      if percentage <= (i * 0.1):
        percentile["<"+str(i*10)] += 1
        percentile[">100"] -= 1 # No longer assumed to be greater than 100% error
        break  
  return percentile

# Setting up the pen for the turtle chart
pen = turtle.Turtle()
pen.write("Percent Error")

# Setting the pen to the bottom left corner
pen.penup()
pen.setpos(-380, -212)
pen.pendown()

def drawBar(height, interval, highest_number):
  '''
  Function to draw a bar of a height corresponding to the values in 'percentile'.
  Input: height - a number, in this case, the total number of percentege errors 
  within a certain percentage range.
  interval - The string key of the percentile formulated as "<10" to ">100"
  Output: draws a bar for each height, producing a bar graph.
  '''
  # Creates a ratioed number to make the graph fit on the screen
  totalHeight = (height/highest_number)*300 # 300 is the height of the tallest

  pen.up()
  pen.forward(25)
  pen.down()
  pen.fillcolor("purple")
  pen.begin_fill()
  pen.left(90)
  pen.forward(totalHeight)
  # Writes the label for each interval at the top of the bar
  pen.write(str(height) + " at " + interval)
  pen.right(90)
  pen.forward(40)
  pen.right(90)
  pen.forward(totalHeight)
  pen.left(90)
  pen.end_fill()
