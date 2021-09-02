# Factorial Example
# Daniel Nguyen
# November 30th, 2020

def factorial(n):
  # Base case
  if n == 0:
    return 1
  else:
    return n*factorial(n-1)

print(factorial(0))
print(factorial(1))
print(factorial(2))
print(factorial(3))
