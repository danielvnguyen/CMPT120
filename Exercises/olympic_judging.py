# Olympic Judging
# Daniel Nguyen
# Oct 2nd, 2020

total_score = 0
print("Score out of 10:")
for i in range(5):
  judge_score = float(input("Judge " +str(i+1) + ": "))
  total_score += judge_score
print("Total Olympic Score is: " + str(total_score/5))
