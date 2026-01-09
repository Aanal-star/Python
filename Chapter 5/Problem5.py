words = {
    "madad":"Help",
    "Kursi":"Chair",
    "Bili":"Cat"
}
word = input("Enter word you want meaning of: ")
print(words[word])

s = set()
n = input("Enter number 1: ")
s.add(int(n))
n = input("Enter number 2: ")
s.add(int(n))
n = input("Enter number 3: ")
s.add(int(n))
n = input("Enter number 4: ")
s.add(int(n))
n = input("Enter number 5: ")
s.add(int(n))
n = input("Enter number 6: ")
s.add(int(n))
n = input("Enter number 7: ")
s.add(int(n))
n = input("Enter number 8: ")
s.add(int(n))
print(s)

s = set()
s.add(18)
s.add("18")
print(s)

set = set()
set.add(20)
set.add("20")
set.add('20')
print(len(set))

d = {}
name = input("Enter friends name")
lang = input("Enter language name")
d.update({name: lang})
name = input("Enter friends name")
lang = input("Enter language name")
d.update({name: lang})
name = input("Enter friends name")
lang = input("Enter language name")
d.update({name: lang})
name = input("Enter friends name")
lang = input("Enter language name")
d.update({name: lang})
print(d)
# if we enter same name then it will update.values can be same but not key

s1 = {8,7,12,"Aanal",[1,2]}
s[4][0]= 9
# we cann't update as list is there