#WAP to fill the letter template given below with name and date
 
letter = '''
               Dear <|Name|>,
               You are selected!
               <|Date|>
               '''


# solution:

print(letter.replace("<|Name|>","Nav").replace("<|Date|>", "2 january 2026"))