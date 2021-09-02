# Palindrome ABBA (Iterative Method and Recursive Method)
# Daniel Nguyen
# December 2nd, 2020

# Iterative Method:
# Returns True if word is a palindrome, false otherwise.
# Use a loop
def is_palindrome(word):
  i = 0
  j = len(word)-1
  # While we're not in the middle
  while i <= j:
    # If the first and last letter aren't the same
    if word[i] != word[j]:
      return False
    # Iterate i and j
    i += 1
    j -= 1
  return True

# Recursive Method:
def is_palindrome_r(word):
  # True base case: 1 letter left, it's a palindrome.
  if len(word)<2:
    return True
  # False base case:
  elif word[0] != word[-1]:
    return False
  # Call to itself, moving closer to the base case.
  # Return so it's a fruitful function.
  else:
    return is_palindrome_r(word[1:-1])

print(is_palindrome("ABBA"))
print(is_palindrome("ABCBA"))
print(is_palindrome("ABC"))

print(is_palindrome_r("ABBA"))
print(is_palindrome_r("ABCBA"))
print(is_palindrome_r("ABC"))
