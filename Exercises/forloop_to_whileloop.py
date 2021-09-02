# Consider the following program:  

colours = ['Red', 'Green', 'Blue', 'Yellow', 'Pink'] 

for i in range(0, len(colours), 2): 

     print (colours[i]) 

# Rewrite the program above using a while loop instead of a for loop. 
# Upload a file called q1.py  with your solution.

colours = ['Red', 'Green', 'Blue', 'Yellow', 'Pink'] 

position = 0
while position < len(colours):
  print(colours[position])
  position += 2
