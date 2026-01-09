# volatile -> no data persistent 
f = open("/Users/aanalmehta/Desktop/Python/Chapter 9/file.txt")
data = f.read()
print(data)
f.close

st = "Hello , you are amazing"
f = open("/Users/aanalmehta/Desktop/Python/Chapter 9/files.txt","w")
f.write(st)
f.close

f = open("/Users/aanalmehta/Desktop/Python/Chapter 9/myfiles.txt")
lines = f.readlines()
print(lines, type(lines))
f.close()

# line = f.readline()
# while(line != ""):
#     print(line)
#     line = f.readline()
# f.close()

# append
str = "qwertyuioplkjhgfdsazxcvbnm"
f = open("/Users/aanalmehta/Desktop/Python/Chapter 9/myfiles.txt","a")
f.write(str)
f.close()


with open("/Users/aanalmehta/Desktop/Python/Chapter 9/myfiles.txt") as f :
    print(f.read())
