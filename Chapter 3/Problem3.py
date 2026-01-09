name = input("Enter your name: ")
print(f"Good Afternoon, {name}")


letter = ''' Dear <|Name|>, 
             You are selected!
             <|Date|>'''
print(letter.replace("<|Name|>","Aanal").replace("<|Date|>","30June"))


namee = "Aanal is good  girl"
print(namee.find("girl"))
# other than space/double space we can also gind other thing ,if not there it will return -1

print(namee.replace("  "," "))