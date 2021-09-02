# Filter Examples
# Daniel Nguyen
# Nov 27th, 2020

# Takes a list of integers and returns only those that are even

# Returns True if x is even
def isEven(x):
  return x%2 == 0

# Returns True if is an alphabet letter
def my_isalpha(s):
  return s.isalpha()

# Test number list:
num_list = [1,2,3,4,5,6,7]
print(list(filter(isEven,num_list)))

# Test string list:
string_list = ["12","abc","13.5","Boop","abc123"]
print(list(filter(my_isalpha,string_list)))
