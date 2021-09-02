# Write a CoffeeBot that asks if you would like cream. 

# It should accept Yes/yes or No/no as inputs, and reply appropriately depending on the answer. 

# If the user inputs anything else, it should repeat back their answer and say that it does not understand.

answer = input("Would you like cream? ")

if answer == "Yes" or answer == "yes":
  print("Here is your cream")

elif answer == "No" or answer == "no":
  print("No cream for you!")

else:
  print("*backs away slowly*")
