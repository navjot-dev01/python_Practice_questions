# WAP to accept marks of 6 student and display them in sorted manner

# marks=[]

# m1=int(input("Enter the marks of 1st student:"))
# marks.append(m1)

# m2= int(input("enter the marks of 2nd student:"))
# marks.append(m2)

# m3= int(input("enter the marks of 3rd student:"))
# marks.append(m3)

# m4= int(input("enter the marks of 4th student:"))
# marks.append(m4)

# m5=int(input("enter the marks of 5th student:"))
# marks.append(m5)

# m6= int(input("enter the marks of 6th student:"))
# marks.append(m6)

# marks.sort()                              # it sorted it alphabetically e.g. ( 0,012 , 100,123,34,356,)  first 0 terms then 1 then 2 because the no. 
#                                           # are in string , if we want integer then 'int(int(input())' use
# print(marks)


                     # SHORT METHOD

marks=[]

for i in range(6):
    m=int(input(f"enter the marks of {i+1} students :"))  # if i use {i+1} then output like this : ;enter the marks of 1 student',without this no no. represent
    marks.append(m)

    marks.sort()
    print("sorted marks are:",marks)

                      # ULTRA - SHORT METHOD

marks=[int(input(f'Enter marks of students:'))  for i in range(6)]
marks.sort()
print(marks)