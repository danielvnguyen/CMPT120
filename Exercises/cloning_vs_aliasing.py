# Cloning vs. Aliasing Examples 
# Daniel Nguyen
# Nov 9th, 2020

# consider a list, which is mutable
a = [1,2,3]
b = a # b is an alias of a

print("a",id(a),a)
print("b",id(b),b) #b has the same address as a 

# Cloning (multiple ways)
c = a[:] # c is a clone of a
d = list(c) # d is a clone of a
e = [1,2,3] # create list again, clone of a.

print("c",id(c),c)
print("d",id(d),d) # clones DONT have same address
# so clones take up new spaces in memory, alias do not.

# Also, if you change the alias 'b', it also changes the list in 'a'
b[0] = 'x'
print('a',id(a),a)
print('b_mod',id(b),b)

# Note: for tuples, aliasing and cloning just point
# to the original, same object. so same addresses.
a = (1,2,3)
b = a
c = (1,2,3)
print("tuple a",id(a),a)
print("tuple b",id(b),b)
print("tuple c",id(c),c)
