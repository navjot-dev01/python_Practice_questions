# Write a python function  to remove a given word from list and strip it at thee same time

def rem(l,word):
    for item in l:
        l.remove(word)             # by this you only remove word not strip it from word
        return l

l=["Harry","Rohan","shubham","ankit","an"]

word=input("Enter the word you want to remove:")
print(rem(l,word))                       

 #                   strip from every word

def rem(l,word):
    n=[]
    for item in l:
       if(item!= word):
           n.append(item.strip(word))
    return n   

l=["Harry","Rohan","shubham","ankit","an"]

word=input("Enter the word you want to remove:")
print(rem(l,word))                       