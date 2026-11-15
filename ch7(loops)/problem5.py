# WAP to find the sum of first n natural number using while loop

num=int(input("Enter the number upto for which you want addition:"))

i=1 # if i write i=0 then not a big problem because i write <=
sum=0
while(i<=num):
    sum+=i
    i+=1

print(f"sum of upto {num} is {sum} ")