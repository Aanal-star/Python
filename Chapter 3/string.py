# string can be in  "", '', ''' '''
# string is immutable(menas can not be changed)
name = "Aanal Mehta"
shortname = name[0:3]
# it include 0,1,2
print(shortname)
character1 = name[1]
print(character1)

print(name[-4:-1])
print(name[1:4])

print(name[:4])#0 to 4
print(name[1:])

word="amazing"
print(word[1:6:2])

# functions:-
print(len(name))
print(name.endswith("l"))
print(name.startswith("AA"))
print(name.capitalize())#only first letter is capital
print(name.title)#cpaitalize each letter of every word
print(name.upper())
index = name.find("Aanal")
print(index)
replace = name.replace("Mehta", "Aanal")
print(replace)

sentence = "There is \'book\'.\nIt is kept inside \tthe \"cupboard\""
print(sentence)