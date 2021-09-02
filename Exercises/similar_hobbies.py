hobbies_1 = input("Person 1, Please enter hobbies separated by spaces: ")
hobbies_2 = input("Person 2, please enter hobbies separated by spaces: ")
hobbies_1 = hobbies_1.split()
hobbies_2 = hobbies_2.split()

hobbies_in_common = 0

for hobby in hobbies_1:
  if hobby in hobbies_2:
    hobbies_in_common += 1
print("You have: " + str(hobbies_in_common) + " hobbies in common!")
