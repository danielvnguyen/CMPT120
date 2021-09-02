# Selection Sort Function
# Daniel Nguyen
# November 20th, 2020

def selection_sort(lst):
  output_list = []
  # Outer loop
  for i in range(len(lst)):
    # Variables to find min number in inner loop
    min_number = lst[i]
    min_index = i
    # Inner loop finds smallest number in sublist
    for j in range(i+1, len(lst)):
      if lst[j] < min_number:
        min_number = lst[j]
        min_index = j
    # Once have smallest element, swap with current element in our outer loop.
    lst[i], lst[min_index] = lst[min_index], lst[i]
  return lst

test_list = [1,52,623,124,2]
print(selection_sort(test_list))

# Note: there is O(n^2) for the complexity (usage of n within n - nested for loop)
