#                  Method of sets

s={1,2,3,4,4,4,"Harry"}              # no repitition allowed
print(s)

print(len(s))

s.add("Banana")
print(s)

s.remove(4)
print(s)

s.pop()                                 # remove arbitrary elements
print(s)

s.clear()                            # remove all elements
print(s)

s.discard(5)                            # if item is not present then it print set, not error
print(s)

s.update([34,56,"Neha"])
print(s)

a={ 2,3,4}
b={4,5,6,7,8}
print(a.union(b))

print(a.intersection(b))

print(a.difference(b))                 # a-b = {2,3,4}-{4,5,6,7,8}= {2,3}
print(b.difference(a))

# symmetric difference
c=a.symmetric_difference(b)               # a-b={2,3,4}-{4,5,6,7,8}={2,3,5,6,7,8}
print("Set A:",a)
print("Set B:",b)
print("Symmetric Difference:",c)

a.symmetric_difference_update(b)
print("After symmetric difference update:")    # update means value of a change with symmetric difference       
print("Set_A:",a)
print("set_B:",b)
print(a.difference(b))
print(a.symmetric_difference(b))
# print(a.symmetric_difference_update(b))      # output = none because in print  & affect next line code output
a.symmetric_difference_update(b)
print(a)


