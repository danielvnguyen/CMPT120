# How to Measure Things in Canada
# Daniel Nguyen
# Date: Sept. 25th, 2020

print("I can tell you what to use for measurements in Canada!")
measure = input("What are you measuring (mass/volume)? ").lower().strip(".!")

# Left branch - mass. If weight, lbs. Otherwise kg
if measure == "mass":
  is_weight = input("Is it your weight?").lower()
  if is_weight == "yes":
    print("Use lbs.")
  else: #make sure if and else are matched up
    print("Use kg.")

# Right branch - volume. If cooking, cups & spoons. Otherwise metric.
elif measure == "volume":
  # TODO: Add this branch
  is_cooking = input("Is it for cooking?").lower()
  if is_cooking == "yes":
    print("Use metric!")
  else:
    print("Use cups and spoons.")
