# Map Examples
# Daniel Nguyen
# Nov 27th, 2020

# Multiply each number in the list by 3

# Return three times the number x
def triple(x):
  return x*3

test_list = [5,2,3,69,420]

# Apply map using triple on the test list
print(list(map(triple,test_list)))
