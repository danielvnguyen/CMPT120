# Question 7: 
# Write program that asks user to input a sequence of integers separated by commas, then print a list that only includes the integers greater than 5. Do this with for/while loops and with filter/map/reduce.

# For/while loop method:
input_list = input("Enter a sequence of integers separated by commas: ")
num_list = input_list.split(',')
result_list = []
for i in range(len(num_list)):
  if float(num_list[i]) >= float(5):
    result_list.append(num_list[i])

print(result_list)

# Filter method:
def greater_than_five(x):
  if float(x) >= float(5):
    return x

input_list = input("Enter a sequence of integers separated by commas: ")
num_list = input_list.split(',')

print(list(filter(greater_than_five,num_list)))
