# McDoland's
# Daniel Nguyen
# Oct 2nd, 2020

print("Answer yes or no:")
ordered_burger = input("Would you like a burger for $5? ").lower()
ordered_fries = input("Would you like fries for $3? ").lower()

total = 0

if ordered_burger == "yes":
  total +=5
if ordered_fries == "yes":
  total +=3

taxed_total = total*1.14
print("Your total with tax is: " + str(round(taxed_total,2)))
