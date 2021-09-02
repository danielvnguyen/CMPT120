# Title: Horoscope Bot
# Author: Daniel Nguyen
# Date: September 16, 2020

# Greet user and ask for year of birth
horoscope = input ("Hello! I'm the Horoscope Bot. What year were you born? ")

if horoscope == "2002" or horoscope == "1990":
  print ("You're a horse!")

elif horoscope == "2003":
  print ("You're the goat!")

else: 
  print ("What year is that?!")

# Use % to compact this code even further.
# ex. if birth year % 12 = 6:
