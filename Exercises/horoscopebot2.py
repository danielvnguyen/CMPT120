# Horoscope Bot ++
# Daniel Nguyen
# Sept 21st, 2020

# Ask the user to enter their year of birth
print("Please enter the year you were born: ")

# Get the year
year = input()
cleaned_year = year.strip("!., ")

# Get the year (quick version)
# year = input().strip("!., ")

# Make a list of numbers
pig_years = ["1935", "1947", "1959", "1971", "1983", "1995"]

# Check if they're a particular horoscope 
if year in pig_years:
  print("You are a pig!")

# Don't know
else:
  print("I'm not sure of your horoscope!")
