# Star Wars Bot
# Daniel Nguyen
# Sept 25th, 2020

print("I will decide if you can join the Dark Side.")
favourite_colour = input("Is red your favourite colour? ").lower()
capes = input("Do you like capes? ").lower()
if favourite_colour == "yes" or capes == "yes":
  print("Dark Side it is!")
else:
  print("Light Side I see.")
