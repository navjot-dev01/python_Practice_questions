#   issubset()

a={1,2}
b={1,2,3}

print(a.issubset(b))     #  a is subset of b if all elements of a is present in b
print(b.issuperset(a))  # b is superset of a if it contain all elements of a 
print(a.isdisjoint(b))       # no common elements