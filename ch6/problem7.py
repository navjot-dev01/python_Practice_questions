#WAP to check the given post is talking about "Harry" or not

post= input("Enter the post:").capitalize()

if("Harry".capitalize() in post):                              # even if about " Harry " space between "  and H &   y and " , it give error
      print("This post is talking about Harry")

else:
    print("This post is not talking about Harry")


    # we can also use .lower() instead of .capitalize()
