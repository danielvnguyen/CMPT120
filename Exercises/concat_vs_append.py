# Concatenate vs. Append
# Daniel Nguyen
# Nov 9th, 2020

myList = []
for i in range(4):
  myList = myList + [i] #note each i has a different id
  print(id(myList))
print(myList)

anotherList = []
for i in range(4):
  anotherList.append(i) #each i now has same id, more efficent than concatenation
  print(id(myList))
print(myList)
