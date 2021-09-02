# Linear Search 
# Daniel Nguyen
# November 16th, 2020

lst_num = [ 22, 6, 122, 21, 36, 24, 46, 67, 44, 88, 10 ]
lst_str = ["a","x","z","p"]

# Can we search the list for a given search term?

# Input: a list of numbers or strings
# Output: a Boolean (whether or not item is in list)
def linear_search_bool(input_list,item):
  for elem in input_list:
    if elem == item:
      return True
  else:
    return False

# With a while loop
def linear_search_bool_while(input_list,item):
  found = False
  i = 0
  while i < len(input_list) and not found:
    if input_list[i] == item:
      found = True
    i += 1 
  return found 

# Getting index we found the element (position)
# Returns None if not found.
def linear_search_index(input_list,item):
  for i in range(len(input_list)):
    if input_list[i] == item:
      return i
  return None 

# Getting indices of found element(s)
# Returns list of indices or None
def linear_search_indices(input_list,item):
  found_list = []
  for i in range(len(input_list)):
    if input_list[i] == item:
      found_list.append(i)
  return found_list

#print(linear_search_index(lst_num,4))
#print(linear_search_index(lst_num,14))

#print(linear_search_bool(lst_num,4))
#print(linear_search_bool(lst_num,14))

print(linear_search_bool_while(lst_num,55))
#print(linear_search_bool_while(lst_num,14))
