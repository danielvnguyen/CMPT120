# Lists are passed by reference!
# Daniel Nguyen
# Nov 9, 2020

def sub_one(num_list):
  for i in range(len(num_list)):
    num_list[i] = num_list[i]-1
  return num_list

alist = [5,5,5,5]
new_list = sub_one(alist)

print(alist) # alist passed by reference, changes.
# do tuple instead if u dont want it to change.
print(new_list)
