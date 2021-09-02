# Greeting Bot
# Daniel Nguyen
# Sept 21st, 2020

# String examples of string methods
# print("!Good!".lower().strip(!)) = "good"
# print("Good!...".strip("!.")) = "Good"

print ("How's it going?")

reply = input()

if reply.lower() == "good":
  print("Great, what went well? ")
  good_thing = input()
  print good_thing.strip(".") + "? That's great."

elif reply == "Bad":
  print("Oh no!")

else:
  print("I see..")
