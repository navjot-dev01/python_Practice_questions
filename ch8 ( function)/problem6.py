# write a python function which converts inches to cms

def inch_to_cms(inch):
    return inch*2.54

inch=float(input("enter the value of inches:"))
print(f' The corresponding value in cms if {inch_to_cms(inch)}')