#  Attempt problem 1 using while loop:

num=int(input("Enter the number for which you want multiplication table:"))

i=0
while(i<11):
    print(f"{num} X {i}={num*i}")
    i+=1