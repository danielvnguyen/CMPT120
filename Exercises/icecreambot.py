# Title: Icecream Scoops
# Author Name: Daniel Nguyen
# Date: October 4th, 2020
# Description: Ask the user if he or she would like to add a certain flavour icecream scoop to their cone. If the user says yes, the scoop will be added ontop and the total price will go up for that scoop. If the user says no, the program will move on to the next scoop, or if at the end, tell the user the total price.

# Instructions: Must incorporate numeric user input, a float, use at least one of the number operators we saw in class + - / *. It should use an accumulation pattern with a loop. It should use at least one conditional statement comparing numbers.

print("Hello, welcome to the Icecream_Shop_Program! Each scoop is $4! Tax is 15%.")
print("Please reply with the number of scoops you want for each flavour:")

wants_mint = int(input("How many mint flavoured scoops would you like? "))
wants_cookie = int(input("How many cookie dough flavoured scoops would you like? "))
wants_bubblegum = int(input("How many bubblegum flavoured scoops would you like? "))
wants_vanilla = int(input("How many vanilla flavoured scoops would you like? "))
wants_chocolate = int(input("How many chocolate flavoured scoops would you like? "))

total_scoops = (wants_mint + wants_cookie + wants_bubblegum + wants_vanilla + wants_chocolate)

total_price = 0

for i in range(total_scoops):
  total_price += 4

if total_scoops <= 0:
  print("Sorry! Your order was either no scoops, or somehow, negative scoops! Come again!")

else:
  total_price = float(total_price * 1.15)
  print ("Okay! Your total price is $" + str(round(total_price,2)) + " with tax.")
