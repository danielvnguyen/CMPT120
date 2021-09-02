# Question 5:
# Binary search function that takes 2 parameters, a sorted list of tuples, and a value to search for within it. 

# Basic binary search algorithm
def binarysearch(lst, value):
  # Initialize first and last element of list
  # Note: binary search is of sorted lists.
  first = 0
  last = len(lst)-1
  # While first less than last
  while first <= last:
    # Variable for middle of list
    mid = (first+last)//2
    # If value is the middle element, return
    if lst[mid][0] == value:
      return lst[mid][1]
    # Otherwise, see if element above or below mid
    elif lst[mid][0] < value:
      first = mid+1
    else:
      last = mid-1
  return -1


test_list = [(0, "Introduction"), (1, "Chatbots"), (2, "Rec Systems"), (3, "Under the hood"), (4, "Graphics"), (5, "Computer Vision"), (6, "Internet and Big Data")]
print(binarysearch(test_list,3))
print(binarysearch(test_list,0))
