print(1==1.0)          #compares values
print(1 is 1)           # compares memory location
print(1 is 1.0)     

# WAP to create a dictionary of hindi words with values as their English translation . Provide user an option to look it up!

words={
    "Keeda":"worms",
    "Zindagi":"life",
    "samay":"Time"
}
word=input("Enter the word you want meaning of:")

print(words[word])               

#  WHY use square bracket instead of parenthesis

#  . paenthesis() is used to call function
#  . dictionaries are accessed using keys, not by calling them like a function
#  . [] act like index
#  . [] used for indexing / key access