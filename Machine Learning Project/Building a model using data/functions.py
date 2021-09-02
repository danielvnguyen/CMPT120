import turtle

def getProcessedData():
  '''
  Gets the data from the file SeoulBikeData.csv in an organized fashion
  Input: None
  Output: Tuple of the bikes rented and other daily information
  '''
  # Openning the file and converting it to a list
  bike_data_file = open("SeoulBikeData.csv")
  bike_data_file.readline() # Skips the header row
  bike_data_file = list(bike_data_file)

  # Output Variable
  bikesRented = []
  # Input Variable
  hourlyData = []

  for i in range(len(bike_data_file)):

    # Building input and output lists
    row = bike_data_file[i]
    bikesRented.append((row.split(",")[1])) # Gets the bikes rented
    hourlyData.append((row.split(",")[2:11])) # Values from column 3 to 11

    # Making values in bikes rented into floats
    bikesRented[i] = float(bikesRented[i])
    
    # Making values in the hourly data into floats
    hourlyRow = hourlyData[i] # Gets a list of the hourly data for a specific hour
    
    # Goes through all the information in hourly data and convert it to a float
    for n in range(len(hourlyRow)): 
      hourlyRow[n] = float(hourlyRow[n])
      
  return (bikesRented, hourlyData)


def calculateError(test_output, outcome):
  '''
  Gives the percent error of the program's predicted data as a dictionary of percentiles
  Input:
  test_output: List of how many bikes were actually rented
  outcome: List of how many bikes were predicted to be rented
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
pen.setpos(-450, -212)
pen.pendown()

def drawBar(height, interval):
  '''
  Function to draw a bar of a height corresponding to the values in 'percentile'.
  Input: height - a number, in this case, the total number of percentege errors 
  within a certain percentage range.
  interval - number corresponding to interval between 0 to 100.
  Output: draws a bar for each height, producing a bar graph.
  '''
  pen.up()
  pen.forward(25)
  pen.down()
  pen.fillcolor("lightpink")
  pen.begin_fill()
  pen.left(90)
  pen.forward(height)
  # Writes the label for each interval at the top of the bar
  pen.write(str(height) + " at " + interval)
  pen.right(90)
  pen.forward(50)
  pen.right(90)
  pen.forward(height)
  pen.left(90)
  pen.end_fill()
