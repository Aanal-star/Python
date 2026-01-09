a1 = int(input("Enter number 1 :"))
a2 = int(input("Enter number 2 :"))
a3 = int(input("Enter number 3 :"))
a4 = int(input("Enter number 4 :"))
if(a1>a2 and a1>a3 and a1>a4):
    print("Greatest number is a1", a1)
elif(a2>a1 and a2>a3 and a2>a4):
    print("Greatest number is a2", a2)
elif(a3>a2 and a3>a1 and a3>a4):
    print("Greatest number is a3", a3)
elif(a4>a2 and a4>a3 and a4>a1):
    print("Greatest number is a4", a4)


marks1 = int(input("Enter marks of subject 1: "))
marks2 = int(input("Enter marks of subject 2: "))
marks3 = int(input("Enter marks of subject 3: "))
total_percentage = (100) * (marks1 + marks2 + marks3)/300
print(total_percentage)
if(total_percentage>=40 and marks1>=33 and marks2>=33 and marks3>=33):
    print("Pass")
else:
    print("Fail")


# spam comment is defined as a text containing following keyword :
# "Make a lot of money" ,"buy now", "suscribe this", "click this"
p1 = "Make a lot of money" 
p2 = "buy now"
p3 = "suscribe this" 
p4 ="click this"
message = input("Enter your comment")
if((p1 in message) or (p2 in message) or (p3 in message) or (p4 in message)):
    print("This is spam")
else:
    print("THis is not spam")


username = input("Enter name: ")
if(len(username)<10):
    print("Less than 10 character")
else:
    print("All is well")


l =["A","B","C","D","E"]
name = input("Enter name:")
if(name in l):
    print("Your name is in list")
else:
    print("Not in list")


markss = int(input("Enter your marks"))
if(markss<=100 and markss>=90):
    grade ="Ex"
elif(markss<=90 and markss>=80):
    grade ="A"
elif(markss<=80 and markss>=70):
    grade ="B"
elif(markss<=70 and markss>=60):
    grade ="C"
elif(markss<=60 and markss>=50):
    grade ="D"
elif(markss<=50 ):
    grade ="F"
print("Your grade is" , grade)


post = input("Enter post")
if("Aanal".lower() in post.lower()):
    print("This post is talking about Aanal")
else:
    print("Not talking about Aanal")