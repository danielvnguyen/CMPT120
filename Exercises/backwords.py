def backwords(word):
  # Base case: when length of word is 1, just return the 1 letter.
  if len(word) == 1:
    return word
  else:
    # Otherwise, call the function on the word without the first letter.
    # and the first letter is added to the end after each call.
    return backwords(word[1:]) + word[0]

word = str(input("Enter the string to be reversed: "))
print(backwords(word))
