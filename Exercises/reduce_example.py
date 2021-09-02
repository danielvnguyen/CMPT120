# Reduce Examples
# Daniel Nguyen
# Nov 27th 2020

# Import reduce function from functools module
from functools import reduce

# Get the sum total of all elements in a list
def add(x,y):
  return x+y #make str if concatenating string and integers

nums = [2,2,2,2]
letters = ["a","b","c"]
alphanumeric = ["a",1,"c",2]

print(reduce(add,nums))
#print(reduce(add,letters))
#print(reduce(add,alphanumeric))
