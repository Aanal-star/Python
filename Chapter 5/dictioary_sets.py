marks = {
    "Aanal" : 100,
    "Dhairya": 90
}
# empty dictionary will like d = {}
print(marks, type(marks))
print(marks["Aanal"])
# dictionary id unordered,mutable,indexed,cannot duplicate keys,mutable
print(marks.items())
print(marks.keys())
print(marks.values())
marks.update({"Aanal":99,"Bhumika":89})
print(marks)
print(marks.get("Nilesh"))
print(marks.get("Aanal"))
print(marks["Aanal"])
# square bracket it will give error if element is not present and round bracket will represent none


# set => collection of well defined objects(non-repeated),cannot access by index
e = set()#empty set
s = {1,5,32,54,5,5,5,"Aanal"}
print(s)
# methods
s.add(566)
print(s,type(s))
s.remove(1)
print(s,type(s))
# pop remove any random element, clear will empty set
s1={1,45,6}
s2={7,8,1,78}
print(s1.union(s2))
print(s1.intersection(s2))
print(s1-s2)