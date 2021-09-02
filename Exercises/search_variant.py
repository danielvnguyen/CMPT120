import statistics

# Linear search function that given a list 'lst' of length n and an item we want to find, searches lst from the beginning AND from the back: lst[0], lst[n-1], lst[1], lst[n-2], lst[2]... and prints True if the item is found and False otherwise. 
def search_variant(lst,item):
  '''
  Input: lst - list of unsorted elements
  item - a specific element to search for in the list
  Output: whether the element is in the list or not.
  '''
  front = 0
  back = len(lst) - 1
  while front <= back:
    if lst[front] == item or lst[back] == item:
      return True
    front += 1
    back -= 1
  return False
