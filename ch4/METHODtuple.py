#         Methods of tuple

a=(23, 455.6 , "Manpreet","Bhavesh",1000,True,1000)
print(a)

no = a.count("Manpreet")                        # ITEM COUNT OCCUR HOW MANY TIME
print(no)

no1 = a.count(1000)
print(no1)

no2 = a.index(455.6)                            # FIND INDEX 
print(no2)

                                                #  ADDING OF TUPLE

b=( "Bird","Animal","<>")
concatenated = a+b
print(concatenated)

                                                # REPITITION OF TUPLE

tuple=(33, 76.5555,"GANGA","LIFE")        
repitition=tuple*3
print(repitition)       

                                                # Membership ( check the item exist in a tuple using 'in' keyword)
print(2 in tuple)
print("GANGA" in tuple)                     

                                                # Length ( 'len()')
print(len(a))
print(len(tuple)) 

                                                # SLICING ( it create new tuple from a subset of the original)
sliced = tuple[1:3]
print(sliced)

                                                # UNPACKING ( tuple can be unpacked into individual variable)

my_tuple=(1,2,3,4,"LIFE")
a,b,c,d,e = my_tuple
print(a,b,c,d,e)
