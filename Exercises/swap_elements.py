# Swap Elements
# Daniel Nguyen
# Nov 16th 2020

numbers = [1,2,3,4,5]

# Swap the elements at index 0 and 1
numbers[0],numbers[1] = numbers[1],numbers[2]
print(numbers)

# Iterate over a sublist from index 3 to end
for i in range(3,len(numbers)):
  print(numbers[i])

# Selection Sort
# Input: unsorted list of numbers
# Output: a sorted list of numbers in input_list
def selection_sort(num_list):
  for i in range(len(num_list)):
    min_number = num_list[i]
    min_number_index = i

    for j in range(i+1, len(num_list)):
      if num_list[j] < min_number:
        min_number = num_list[j]
        min_numer_index = j

    num_list[min_number_index], num_list[i] = num_list[i], num_list[min_number_index]

  return num_list

test_input = [39,2,103,42,50,61]
print(selection_sort(test_input))
