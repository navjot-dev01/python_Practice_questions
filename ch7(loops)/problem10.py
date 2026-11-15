
# for i in range(5):
#     print("*",end=" ")
    

# i) WAP to print multiplication table of n by for loop in reverse loop
# ii) WAP to print multiplication table of n by for loop in rverse loop , table is upto 10,20,...200.. take entry from user
n=int(input("Enter the number: "))

for i in range(1,11):
    print(f" {n} x {11-i}={n*(11-i)}")


    # 2 x 1 =2                         2 x 10 =20         2x20=40
    # 2 x 2 =4                         2 x 9 =18          2x19=38                   n x (11-i)=reverse table  upto 10
    # 2 x 3 =6                         2 x 8 =16                                    n x (21-i)=upto 20
    # 2 x 4 =8                         2 x 7 =14
    # 2 x 5 =10                        2 x 6 =12
    # 2 x 6 =12                        2 x 5 =10
    # 2 x 7 =14                        2 x 4 =8
    # 2 x 8 =16                        2 x 3 =6
    # 2 x 9 =18                        2 x 2 =4
    # 2 x 10 =20                       2 x 1 =2         

n=int(input("Enter the number: "))
r=int(input("Enter the  no. upto for which you want multiplication table"))

for i in range(1,r+1):
    print(f" {n}X{(r+1)-i}={n*((r+1)-i)}")
    