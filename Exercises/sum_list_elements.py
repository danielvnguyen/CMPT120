# Sum of elements in a list
# Daniel Nguyen
# November 30th, 2020

def sum(lst):
  # Base case
  if len(lst) == 0:
    return 0
  # Recursive call
  else:
    return lst[0] + sum(lst[1:])

# Assume list is non-empty
num_list_1 = [4]
num_list_2 = [4,5]
num_list_3 = [1,2,3,4,5]

print(sum(num_list_1))
print(sum(num_list_2))
print(sum(num_list_3))
