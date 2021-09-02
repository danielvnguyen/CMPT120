# Tuple examples
# Daniel Nguyen
# Novemeber 6th, 2020

# Make a tuple
max_rgb_values = (255,255,255)
print(max_rgb_values)

# Conversion
my_list = [255,255,255]
my_tup = tuple(my_list)
print(my_tup)

list_rgb_values = list(max_rgb_values)
print(list_rgb_values)

# Make a function that returns a tuple
def return_three_values(a,b):
  """ Returns a tuple
  """
  my_sum = a+b
  my_product = a*b
  my_name = "Daniel"
  return (my_sum, my_product, my_name)

print(return_three_values(3,4))

values = return_three_values(3,4)
print(values[0])
