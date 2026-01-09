class Employee:
    company ="ITC"
    name = "Default name"
    def show(self):
        print(f"The name is  {self.name} and salary is {self.company}")

class coder:
    language = "Python"
    def printlanguage(self):
        print(f"Out of all laguage here is your language: {self.language}")

# class Programmer:
#     company = "ITC Infotech"
#     def show(self):
#         print(f"The name is  {self.name} and salary is {self.salary}")
#     def showLanguage(self):
#         print(f"The name is {self.name} and he is good with {self.language}")
class Programmer(Employee,coder):
    company = "ITC Infotech"
    def showLanguage(self):
        print(f"The name is {self.company} and he is good with {self.language} language")
a = Employee()
b = Programmer()
b.showLanguage()
b.show()
b.printlanguage()
print(a.company,b.company)


# multilevel
class Employee:
    def __init__(self):
        print("Constructor of Employee")
    a = 1
class Programmer(Employee):
    def __init__(self):
        print("Constructor of Programmer")
    b = 2
class Manager(Programmer):
    def __init__(self):
        super().__init__()
        print("Constructor of Manager")
    c = 3
o=Employee()
print(o.a)
o = Programmer()
print(o.b)
o = Manager()
print(o.a,o.b,o.c)


# class method
class Employeee:
    a = 1
    @classmethod
    def show(cls):
        print(f"The value of a is {cls.a}")
    @property
    def name(self):
     return self.ename
    @name.setter
    def name(self,value):
        self.ename = value
e = Employeee()
e.a = 45
e.name = "Aanal"
print(e.ename)
e.show()


#operator overloading
class Number:
    def __init__(self,n):
        self.n = n
    def __add__(self,num):
        return self.n + num.n
n= Number(1)
m = Number(2)
print(n + m)