# 1 
# def avg():
#     a=int(input("Enter the number:"))
#     b=int(input("Enter the number:"))
#     c=int(input("Enter the number:"))

#     average=(a+b+c)/3
#     print(average)

# avg()
# avg()
# avg()
# avg()

# 2

def goodDay(name):
    print("Good Day" + name)

goodDay(" Harry ")


# 3

def goodDay(name,ending):
    print("Good Day"+ name)
    print(ending)

goodDay(" Radhu "," Thankyou ")
goodDay(" Jiya ", " Bye ")
goodDay(" Tamanna "," Thank you ")

# 4

def greet(name):
    gr="Hello"+ name
    return gr

a=greet(" Simran")
print(a)

#5
def greet(name,ending):
    print(" Good day" + name)
    print(ending)
    return "ok"

a=greet(" Nav ","Thank you")
print(a)

# 6
def goodDay(name,ending="Thank u"):     # default function
    print("Good Day" + name)

goodDay("Juhi")    

# 7
def goodDay(name,ending="Thank u"):
    print(f'Good evening { name}')
    print(ending)

goodDay("riya")

# 8
def goodDay(name,ending="thank u"):
    print(f'Good evening {name}')
    print(ending)

goodDay("Tiya","thanks")







