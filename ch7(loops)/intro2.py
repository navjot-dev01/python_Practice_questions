# For loop with else

list=[1,7,8]
for item in list:
    print(item)

else:
    print("Done")

                          # break,continue,pass

for i in range(100):
    if(i==50):
        break               # does not print furthur value of 49
    print("with break:",i)                          



for i in range(100):
    if(i==50):
        continue             # does not print condition and do further process
    print("with continue:",i)



for i in range(100):
    print(i)  
    pass                 # it means if we want to do execute another code instead of 1st code then we write pass for not to execute that progarm

i=0
while(i<6):
    print("hi")
    i+=1
