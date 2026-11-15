#WAP to check that tuple type cannot be changed in python

tuple=(32, 234 ,"DAYA")
# tuple[2]=34

print(type(tuple))

lst = list(tuple)
print(lst)
print(type(lst))