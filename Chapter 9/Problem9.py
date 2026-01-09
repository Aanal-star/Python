import random
f = open("/Users/aanalmehta/Desktop/Python/Chapter 9/poem.txt")
content = f.read()
if("twinkle" in content):
    print("Twinkle is present")
else:
    print("Not preset")
f.close()

def game():
    print("You are playing the game")
    score = random.randint(1,62)
    with open("/Users/aanalmehta/Desktop/Python/Chapter 9/poem.txt") as f:
        hiscore = f.read()
    if(hiscore ==""):
        hiscore = int(hiscore)
    else:
        hiscore = 0
    print(f"Your score: {score}")
    if(score>hiscore):
        with open("/Users/aanalmehta/Desktop/Python/Chapter 9/hiscore.txt","w") as f:
            f.write(str(score))
    return score    
game()


def generateTable(n):
    table = ""
    for i in range(1,11):
        table +=f"{n} * {i} = {n*i}\n"
    with open(f"/Users/aanalmehta/Desktop/Python/Chapter 9/tables/table_{n}.txt","w") as f:
     f.write(table)
for i in range (2,21):
    generateTable(i)



word = "Donkey"
with open("/Users/aanalmehta/Desktop/Python/Chapter 9/myfiles.txt","r") as f:
    content = f.read()
contentNew = content.replace(word, "######")
with open("/Users/aanalmehta/Desktop/Python/Chapter 9/myfiles.txt","w") as f:
    f.write(contentNew)



words = ["Donkey","is","donkey"]
with open("/Users/aanalmehta/Desktop/Python/Chapter 9/myfiles.txt","r") as f:
    content = f.read()
    for word in words:
        contentNew = content.replace(word, "#"*len(words))
with open("/Users/aanalmehta/Desktop/Python/Chapter 9/myfiles.txt","w") as f:
    f.write(contentNew)



with open("/Users/aanalmehta/Desktop/Python/Chapter 9/myfiles.txt","r") as f:
    lines = f.readlines()
lineno = 1
for line in lines:
    if("python" in line):
     print(f"Present {lineno}")
     break
    lineno +=1
else:
     print("Not present")


with open("/Users/aanalmehta/Desktop/Python/Chapter 9/myfiles.txt") as f:
    content = f.read()
with open("/Users/aanalmehta/Desktop/Python/Chapter 9/renamed.txt") as f:
    f.write(content)