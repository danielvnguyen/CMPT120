# eliminateGreen() 
# Daniel Nguyen
# November 6th, 2020

def eliminateGreen(lsts):
  emptylst = []
  for lst in lsts:
    g = lst[1]
    if g >= 0: #green position of RGB 
      lst[1] = 0
      emptylst.append(lst)
  return emptylst

lsts = ([ [100,100,100], [10,255,0], [100,35,255],[10,0,200] ]) 

print(eliminateGreen(lsts))
