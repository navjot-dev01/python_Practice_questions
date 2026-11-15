 # Create an empty dictionary. Allow 4 friends to enter their favorite language as value and use key as their names. Assume that names are unique

# d={}
# name= input("enter friends name:")
# lang=input("enter language name:")

# d.update({name:lang})          # there is no add() method in dict. so we use update()


# name= input("enter friends name:")
# lang=input("enter language name:")

# d.update({name:lang})


# name= input("enter friends name:")
# lang=input("enter language name:")

# d.update({name:lang})


# name= input("enter friends name:")
# lang=input("enter language name:")

# d.update({name:lang})

# print(d)          # if i use same name as key then 2nd or 3rd name print because it give value of.update  . try this , because we use.update 

 
                             # or

d={}
r=int(input("Enter number of friends:"))    
                         
for i in range(r):
    name=input("enter the name of the friend :")
    lang=input("Enter the favorite language of your friend ")
    d.update({name:lang})

print(d)    

