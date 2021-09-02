questions = ["Did you eat? ", "Did you study? ", "Did you do laundry? ", "Did you call grandma? "]

score = 0 #score that would be incremented

for question in questions:
  answer = input(question).lower()
  if answer == "yes":
    score += 1

if score == 0:
  print("I'm coming over.")
elif score == 1 or score == 2:
  print("Ok.")
elif score == 3 or score == 4:
  print("Good!")
