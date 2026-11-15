# WAP to print multiplication table of given number using for loop

num=int(input("Enter the number for which you would like to see the  multiplication table:"))

for i in range(1,11):
    # print(f"{num} x {i} = {num*i}")
    # or
    print(f"{num} x {i} = {num*i} \n{num} {i}s are {num*i}")





# what if i don't put int in num

num=input("Enter the number for which you would like to see the  multiplication table:")

for i in range(1,11):
    # print(f"{num} x {i} = {num*i}")
    # or
    print(f"{num} x {i} = {num*i}" )

