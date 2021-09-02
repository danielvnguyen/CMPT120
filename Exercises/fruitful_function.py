# A simple fruitful function
# Daniel Nguyen
# November 2nd, 2020

# Given parameters a,b, return a^b
def high_power(a,b):
  answer = a**b
  if answer > 10:
    return a**b #beware of return statement
    #here, if answer>10, rest of the function wont run.
  print("It's too low!")

print(high_power(2,2))

# Note: CTRL + / to comment out multiple lines
# answer = power(2,2)
# answer2 = power(answer,2)

# print(answer)
# print(answer2)
