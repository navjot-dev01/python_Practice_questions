# WAP to find out whether the student is failed or passed if it is required total of 40% and at least 33% in each subject to pass . assume 3 
# subjects and take marks as an input from the user 

marks1=int(input("Enter the marks of maths:"))
marks2=int(input("entre the marks of english:"))
marks3=int(input("Enter the marks of science:"))

total_percentage=((marks1+marks2+marks3)*100)/300

if(total_percentage>=40 and marks1>=33 and marks2>=33 and marks3>=33):
    print("You are passed.",total_percentage)

else:
    print("You are failed!",total_percentage)
