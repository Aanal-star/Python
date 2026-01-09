class Employee:
    language = "Python"#class attribute
    salary = "120000"
    def getInfo(self):
        print(f"The language is {self.language}.The salary is {self.salary}")

    @staticmethod#no self needed
    def greet():
        print("Good Morning")
    
    def __init__(self,name,salary,language):#dunder method which is automatically called
        self.name = name
        self.salary = salary
        self.language = language
        print("i am creating object")

# aanal = Employee()
# aanal.name = "Aanal"#instant attribute
# print(aanal.name,aanal.language,aanal.salary)
# dhairya = Employee()
# dhairya.name = "Dhairya"
# print(dhairya.name,dhairya.language,dhairya.salary)


# bhumika = Employee()
# bhumika.language = "Javascript"
# print(bhumika.language)
# bhumika.getInfo()
# bhumika.greet()


# init (constructure) 
nilesh = Employee("Nilesh",130000,"Java")
print(nilesh.name,nilesh.salary)