# list store set of value of any data type
friends =["a","B","4","Aanal",True]
friends[0] = "grapes"
print(friends[0])
# lists are mutable (can be change)
print(friends[1:4])
# lists method
print(friends)
friends.append("Hello")
print(friends)

l1=[1,4,35,88,23,56]
# l1.sort()
# l1.reverse()
# l1.insert(3,333)
# value = l1.pop(3)
# print(value)
l1.remove(56)#pop takes index number and remove takes value
print(l1)


# tupple -> immutable
a = (1,2,3,4,55,"Aanal",False)#empty tupple can be like a =() and if we do a = (1) it is number to make it tupple a=(1,)
print(type(a))
# methods
print(a)
print(len(a))
no = a.count(55)
print(no)

index = a.index(False)
print(index)

b = ("A","B","C")
concate = a + b
print(concate)

repeated = a*3
print(repeated)

print(3 in a)

sliced = a[1:4]
print(sliced)