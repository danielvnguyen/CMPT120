import turtle

def getProcessedData():
  '''
  Gets the data from the file forestfires.csv in an organized fashion
  Input: None
  Output: Tuple of the areas of burned forest and other daily information
  '''
  # Openning the file and converting it to a list
  forest_fire_file = open("forestfires.csv")
  forest_fire_file.readline() # Skips the header row
  forest_fire_file = list(forest_fire_file)

  # Output Variable
  areaBurned = []
  # Input Variable
  dailyData = []

  for i in range(len(forest_fire_file)):

    # Building input and output lists
    row = forest_fire_file[i]
    areaBurned.append((row.split(",")[12])) # Gets the area burned
    dailyData.append((row.split(",")[0:2]) + (row.split(",")[4:12])) # Gets the daily data 

    # Making values in area burnt into floats
    areaBurned[i] = float(areaBurned[i])
    
    # Making values in the daily data into floats
    dailyRow = dailyData[i] # Gets a list of the daily data for a specific day
    
    # Goes through all the information in daily data and convert it to a float
    for n in range(len(dailyRow)): 
      dailyRow[n] = float(dailyRow[n])
      
  return (areaBurned, dailyData)


def calculateError(test_output, outcome):
  '''
  Gives the percent error of the program's predicted data as a dictionary of percentiles
  Input:
  test_output: List of the area of forest fire burned each day
  outcome: List of how much area of the forest fire was predictedly burnt each day.
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

def drawBar(height, interval):
  '''
  Function to draw a bar of a height corresponding to the values in 'percentile'.
  Input: height - a number, in this case, the total number of percentege errors 
  within a certain percentage range.
  interval - The string key of the percentile formulated as "<10" to ">100"
  Output: draws a bar for each height, producing a bar graph.
  '''
  pen.up()
  pen.forward(25)
  pen.down()
  pen.fillcolor("orange")
  pen.begin_fill()
  pen.left(90)
  pen.forward(height*10)
  # Writes the label for each interval at the top of the bar
  pen.write(str(height) + " at " + interval)
  pen.right(90)
  pen.forward(40)
  pen.right(90)
  pen.forward(height*10)
  pen.left(90)
  pen.end_fill()
