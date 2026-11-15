# Write a python function to pevent the first n lines of the following pattern :
#  ***
#  **
#  *

def lines(n):
    if(n==0):
        return 
    print("*"*n)
    lines(n-1)
   

n=int(input("Enter the n number:"))
print(lines(n))              # i don't use print(lines(n)) here because i write print("*"*n) and lines(n-1) 
                      