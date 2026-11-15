
                                    # LIST ARE MUTABLE(changable) and list of list is allowed



name= "Gurleen Kaur"

print(len(name))
print(name.endswith("aur"))
print(name.startswith("gurl"))
print(name.lower())
print(name.capitalize())

                            # LIST INDEXING

list = [3,0,1,34,12,2,98]
list.sort()
print(list)

list.pop()
print(list)

list.append(45)
print(list)

list.insert(1,100)
print(list)

list.pop(2)
print(list)

list.reverse()
print(list)

list.remove(34)
print(list)                               # IF I USE print at last then after all the operations written on above firstly perform and then print    

#                                  LIST SLICING

list1=["Gurleen",3,23,56.98,"Ram",False]

print(list1[0])

list1[4]=222222222
print(list1[4])
print(list1)

print(list1[0:5])
print(list1[:5])

print(list1[4:5])
print(list1[4:])

print(type(list1[2]))
print(type(list1[4])) # changed value 222222222
print(type(list1[3]))
print(type(list1[5]))