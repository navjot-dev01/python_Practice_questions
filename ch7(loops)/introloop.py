for i in range(1,6):          # value comes 1 less than 6
    print("values in range is :",i)           # print upto 5


# while loop
i=1
while(i<6):
    print("values in while loop is:",i)
    i=i+1           # print upto 5



i=0    # print upto 6
while(i<6):
    print("HELLO")
    i+=1


# WAP to print the content of list using while loops
list=[1,"Nav",34.6,False,"Shardha"]
i=0
while(i<len(list)):          # because i=0 if i=1 then len(list)+1
    print("content of list using while loop: ",list[i])
    i+=1

# from for loop:
list=[1,"Nav",34.6,False,"Shardha"]
for i in list:
    print("content of list using for loop:" ,i)


#  RANGE
# range(start,stop,step_size)

for i in range(0,100,5):        # not contain 100 
    print("range using step size:",i)


# print value of tuple:
tuple=(1,2,3,"Love")

for i in tuple:
    print("tuple content using for loop:" ,i)

# print values of string:

string="NaVJOT KAUR"
for i in string:
    print("string content using for loop:" ,i)    


