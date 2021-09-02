# Fruitful Recursion: Decimal to Binary
# Daniel Nguyen
# December 12th, 2020

def toBinary(n):
  convertString = "01"
  # Base case: if n is 0 or 1
  if n < 2:
    return convertString[n]
  # Recursive call
  else:
    return toBinary(n//2) + convertString[n%2]

print(toBinary(0))
print(toBinary(1))
print(toBinary(2))
print(toBinary(3))
print(toBinary(8))
print(toBinary(10))
print(toBinary(100))
