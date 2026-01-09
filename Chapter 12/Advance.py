# valrus
if(n := len([1,2,3,4,5])) > 3:
    print(f"List is too long({n} elements,expected <=3)")

# type defination
n :int =5
name : str ="Aanal"
def sum(a,b)-> int:
    return a + b

from typing import List,Union,Tuple
numbers: List[int] = [1,2,3,4,5]

persons:Tuple[str,int] = ("Aanal",20)

scores: Dict[str,int] = {"Aanal": 20, "Dhairya":17}

identifier: Union[int,str] = "ID123"
identifier = 12345

# match case
def http_status(status):
    match status:
        case 200:
            return "Ok"
        case 404:
            return "Not Found"
        case 500:
            return "Internal server error"
        case _:
            return "Unknown status"
print(http_status(200))


# dictionary merge
dict1 = {'a':1, 'b':2}
dict2 = {'b':3, 'c':4}
merged = dict1 | dict2
print(merged)



# exception handling
try:
    a = int(input("Hey,Enter a number:"))
    print(a)
except ValueError as v:
    print("Heyyyy")
    print(v)
except Exception as e:
    print(e)
else:
    print("Hello,nice")
# if try is correct it will execute else block
finally:
    print("I am inside finially")
# finially is mainly used when function is there. In functio if we write return then simpe statement will not run but finially will



# raising exception
a = int(input("Enter number"))
b  = int(input("Enter second number"))
if(b == 0):
    raise ZeroDivisionError("Our program is not meant to divide with zero")
else:
    print(f"The division a/b is {a/b}")


# importmodule.py
from module import myFunc


# global.py
def fun():
    a =3
    print(a)
    a = 89
    print(a)
fun()

b = 80
def funcc():
    global b
    b = 4
    print(b)
print(b)
fun()

# ENumarate
l = [3,513,45]
index =0
for item in l:
    print(f"The item number {index} is {item}")
    index +=1

for index,item in enumerate(l):
    print(f"The item number {index} is {item}")




# list comprehension
l1 = [1,2,5,9]
# squaredList = []
# for item in l1:
#     squaredList.append(item*item)
# print(squaredList)
squaredList = [i*i for i in l1]
print(squaredList)