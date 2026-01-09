def avg():
    a = int(input("Enter your number"))
    b = int(input("Enter your number"))
    c = int(input("Enter your number"))
    average = (a + b+ c)/3
    print(average)
avg()

def goodday(name,ending):
    print("Good Day " + name)
    print(ending)
    return "ok"
a = goodday("Aanal","Thank You")
goodday("Aanal","Thank You")
print(a)

# default
def goodday(name,ending="Thank You"):
    print("Good Day " + name)
    print(ending)
goodday("Dhairya")
goodday("Dhairyas", "Thanks")


# recursion => call itself
def factorial(n):
    if(n==1 or n==0):
        return 1
    return n * factorial(n-1)
n = int(input("Enter number"))
print(f"Factorial of number is {factorial(n)}")