# Question 6:
# Define a function that merges 2 sorted lists into one big one.
# This is the function that is used as part of the merge sort algorithm. Note that the lengths of the two input lists may be different. Test for 3 different cases.

def merge(lst_one, lst_two):
  # Intialize resulting list variable
  result_list = []
  # While either of the lists still have elements in them
  while(len(lst_one) > 0 or len(lst_two) > 0):
    # if first list empty, add the first element of the 2nd list
    if(len(lst_one) == 0):
      result_list.append(lst_two[0])
      lst_two.pop(0)
    # elif second list empty, add the first element of the 1st list
    elif(len(lst_two) == 0):
      result_list.append(lst_one[0])
      lst_one.pop(0)
    # elif first element of first list > first element of second list, add the first one.
    elif(lst_one[0] < lst_two[0]):
      result_list.append(lst_one[0])
      lst_one.pop(0)
    # else, vice versa.
    else:
      result_list.append(lst_two[0])
      lst_two.pop(0)
  return result_list

test_list = [1, 5, 10, 20]
test_list_two = [3,7,21]
test_list_three = [4,6,18,32]
# Testing 3 different cases:
print(merge(test_list, test_list_three))
#print(merge(test_list, test_list_two))
#print(merge(test_list_two, test_list_three))
