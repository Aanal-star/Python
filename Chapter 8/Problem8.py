a = int(input("Enter number"))
b = int(input("Enter number"))
c = int(input("Enter number"))
def max(a,b,c):
    if(a>b and a>c):
       return a
    elif(b>a and b>c):
        return b
    elif(c>a and c>b):
        return c
print(max(a,b,c))


#temp conversion 
def f_to_C(f):
    return 5 *(f-32)/9
f = int(input("Enter temp in F°"))
print(f"{round(f_to_C(f), 2)} °C")


#sum 
def sum(n):
    if(n==1):
        return 1
    return sum(n-1) + n
print(sum(4))


# patter
def pattern(n):
    if(n == 0):
        return
    print("*" * n)
    pattern(n-1)
pattern(5)


# inches to cm
def convertor(inch):
    return inch * 2.54
n = int(input("Enter in inches"))
print(f"Thge corresponding value in cms is {convertor(n)}")


l = ["A","B","C","D"]
def rem(l,word):
    n = []
    for item in l:
        if not(item == word):
            n.append(item.strip(word))
    return n
print(rem(l,"C"))


def multiply(n):
    for i in range(1,11):
        print(f"{n} * {i} = {n*i}")