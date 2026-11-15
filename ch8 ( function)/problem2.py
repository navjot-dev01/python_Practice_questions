# WAP in python using function to convert celsius to fahrenheit

def temp_conversion(f):
    return 5*(f-32)/9

f=int(input("Enter temperature in F:"))
z=temp_conversion(f)
# print(z)


#° = alt(left hand side vala) + 0176 then release alt 
print(f'{round(z,2)} °C ')                   
