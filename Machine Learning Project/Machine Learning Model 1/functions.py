# Description: Function file with the two functions - createInput and createOutput.

import random

def createInput(length):
  """
  Creates a list of lists with 3 integers from 0-1000
  Input: How many sublists of 3 elements are to be created
  Output: 2d list of the 3 integer values
  """
  # List of 3 element list [[x1,x2,x3]...]
  inputList = []
  
  # Create 100 sublists through iteration
  for i in range(length):
    subList = []

    # Creating the sublist of 3 values from a range from 0-1000
    for n in range(3):
      randomNum = random.randint(0,1000)
      subList.append(randomNum)

    # Adding the completed sublist of inputs to the main list 
    inputList.append(subList)
    
  return inputList

# Creating a 100 of outputs
def createOutput(lst):
  '''
  Creates one list with results for each of the corresponding sublists.
  Input: lst - a list containing 100 sublists with 3 elements in each.
  Output: one list with the resulting value for each of the 100 sublists.
  '''
  # List of length outputs corresponding to the inputs.
  outputList = []

  # Creates a result for each sublist by multiplying the first, second, and third
  # positions of the sublist by 1, 2, and 3 respectively.
  for sublist in lst:
    result = 1*sublist[0] + 2*sublist[1] + 3*sublist[2]

    # Appends the result to outputList
    outputList.append(result)

  return outputList
