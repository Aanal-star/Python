n = int(input("Enter a number: "))
for i in range(1,11):
    print(f"{n} * {i} = {n*i}")
i = 1
while(i<11):
    print(f"{n} * {i} = {n*i}")
    i += 1

l = ["Aanal" , "Dhairya", "Bhumika","Nilesh"]
for name in l:
    if(name.startswith("A")):
        print(f"Hello {name}")


for i in range(2,n):
    if(n % i == 0):
        print("Number is not prime")
        break
else:
    print("Number is prime")

k = 1
totalsum = 0
while k <= n:
    totalsum += k
    k += 1
print(totalsum)

# factorial
product = 1
for i in range(1,n+1):
    product = product * i
print(f"The factorial of {n} is ",product)

# patterns
for i in range(1,n+1):
 print(" " * (n-i), end="")
 print("*" *  (2*i-1), end="")
 print("")

for i in range(1,n+1):
#  print(" " * (n-i), end="")
 print("*" *  (i), end="")
 print("")


for i in range(1, n + 1):
    if (i == 1 or i == n):
        print("*" * n)
    else:
        print("*", end="")
        print(" " * (n - 2), end="")
        print("*", end="")
        print("") 

# 
for i in range(1,11):
    print(f"{n} * {11-i} = {n*(11-i)}")