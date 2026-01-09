class TwoDVector:
    def __init__(self,i,j):
        self.i = i
        self.j = j
    def show(self):
        print(f"The vector is {self.i}i + {self.j}j")
class ThreeDVector(TwoDVector):
    def __init__(self,k,i,j):
        super().__init__(i,j)
        self.k = k
    def show(self):
        print(f"The vector is {self.i}i + {self.j}j + {self.k}k")
a = TwoDVector(1,2)
a.show()
b = ThreeDVector(1,2,3)
a.show()



class Animals:
    pass
class Pets(Animals):
    pass
class Dog(Pets):
    @staticmethod
    def bark():
        print("Bow Bow")



class EMployee:
    salary = 234
    _increment = 20  # Backing variable to avoid recursion
    
    @property
    def salaryAfterIncrement(self):
        return self.salary + (self.salary * (self._increment / 100))
    
    @salaryAfterIncrement.setter
    def salaryAfterIncrement(self, new_total_salary):
        # Calculate what the increment percentage should be based on a new total salary
        self._increment = ((new_total_salary / self.salary) - 1) * 100

e = EMployee()
print(f"Initial: {e.salaryAfterIncrement}") # Output: 280.8
# Using the setter to adjust the increment based on a target salary
e.salaryAfterIncrement = 300 
print(f"New Increment: {e._increment}%")




class Complex:
    def __init__(self,r,i):
        self.r = r
        self.i = i
    def __add__(self , c2):
        return Complex(self.r + c2.r , self.i + c2.i)
    def __mul__(self, c2):
        # Corrected: Use .i instead of .j and apply the multiplication formula
        real_part = (self.r * c2.r) - (self.i * c2.i)
        imag_part = (self.r * c2.i) + (self.i * c2.r)
        return Complex(real_part, imag_part)
    def  __str__(self):
        return f"{self.r} + {self.i}i"
c1 = Complex(1,2)
c2 = Complex(3,4)
print(c1 +c2)
print(c1*c2)




class Vector:
    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z
    def __add__(self,other):
        result = Vector(self.x + other.x, self.y + other.y, self.z + other.z)
        return result
    def __mul__(self,other):
        result = (self.x * other.x + self.y * other.y + self.z * other.z)
        return result
    def __str__(self):
        return f"Vector({self.x}, {self.y}, {self.z})"
        # return f"{self.x}i + {self.y}j + {self.z}k"
    def __len__(self):
        return 3
v1 = Vector(1,2,3)
v2 = Vector(4,5,6)
v3 = Vector(7,8,9)
print(v1 + v2)
print(v1 * v2)
print(v1 + v3)
print(v1 * v3)