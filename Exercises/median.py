import statistics

# Create a function that returns the median of a list of length n. Consider cases: where n is even/odd.
def median(lst):
  lst.sort() # sort from smallest to largest
  length = len(lst)
  if length % 2 == 0: #if the list has an even amount of elements
    median = (lst[length//2] + lst[length//2-1]) / 2 #add 2 middle numbers and / by 2
  else:
    median = lst[(length-1)//2] #gets middle number if odd
  return median

test_lst = [124,2,41,525,252,69]
odd_test_lst = [124,2,41,525,252,69,2]
print(search_variant(test_lst, 9))
print(median(test_lst))
print(median(odd_test_lst))
