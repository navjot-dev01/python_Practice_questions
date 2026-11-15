# can you change the value inside of a list which is contained in set S?

#s={8,9,12,"harry",[1,2]}


# NO , we can't

# . sets stores hashable (immutable) elements              [ non hashable: list, set, dictionary]
#  . list -> mutable -> not hashable                       [ hashable: int , float, string , tuple( with immutable objects)]
#  . list can't be as an element of a set


#                  If use TUPLE

s={8,9,12,"harry",(1,2)}
s.remove((1,2))
s.add((8,9))
print(s)