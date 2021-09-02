# Binary Search
# Daniel Nguyen
# November 25th, 2020

def binarySearch(lst, item):
  first = 0
  last = len(lst) - 1
  found = False

  while first <= last and not found:
    # Get midpoint
    midpoint = (first+last)//2
    # If the midpoint is the item, we're done
    if lst[midpoint] == item:
      found = True
    # Otherwise, change the search space
    else: 
      if item < lst[midpoint]:
        last = midpoint - 1
      else:
        first = midpoint + 1
  return found

test_even = [ 5, 12, 18, 19, 26, 46, 64, 78, 90, 115 ]  
print(binarySearch(test_even,78))
