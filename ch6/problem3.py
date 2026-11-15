# A spam comment is defined if a text containing following keywords:
# " make a lot of money","buy now","subscribe this","click this"
# write a program to detect these spams.


p1="make a lot of money"
p2="buy now"
p3="subscibe this"
p4="click this"

comment=input("Enter the message:").lower()
if ((p1.lower() in comment) or (p2.lower() in comment) or (p3.lower() in comment) or(p4.lower() in comment)):
    print(" Message is spam ")

else:
    print("Message is not spam")

