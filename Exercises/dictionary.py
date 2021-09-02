# Dictionaries examples
# Daniel Nguyen
# Nov 13th, 2020

menu = {"taro":6.99, "matcha":5.50}
print(menu)

menu["watermelon"] = 2.99
print(menu)

for item in menu:
  print(item, menu[item])

# Print length of dictionary, number of elements in dictionary.
print(len(menu))
