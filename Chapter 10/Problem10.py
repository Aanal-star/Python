class Programmer:
    company = "Microsoft"
    def __init__(self,name ,salary,pin):
        self.name = name
        self.salary = salary
        self.pin = pin
p = Programmer("Aanal",120000,24500)
print(p.name,p.salary,p.pin,p.company)


class Calculator:
    def __init__(self,n):
        self.n = n
    def square(self):
        print(f"The square is {self.n * self.n}")
    def cube(self):
        print(f"The square is {self.n * self.n * self.n}")
    def squareroot(self):
         print(f"The square is {self.n **1/2}")
    @staticmethod
    def hello():
        print("Hello There")
a = Calculator(4)
a.hello()
a.square()
a.cube()
a.squareroot()


class Demo:
    a=4
o = Demo()
print(o.a)
o.a = 0
print(o.a)
print(Demo.a)#class attribute is not change but instant attribute is there


import random
class Train:
    def __init__(self,trainNo):
        self.trainNo = trainNo
    def book(self,fro,to):
        print(f"Ticket is book in train number: {self.trainNo} from {fro} to {to}")
    def getStatus(self):
        print(f"Train number: {self.trainNo} is running on time")
    def getFair(self,fro,to):
        print(f"Ticket fair in train number: {self.trainNo} from {fro} to {to} is {random.randint(222,5555)}")
t = Train(12399)
t.book("Rampur","Delhi")
t.getStatus()
t.getFair("Rampur","Delhi")