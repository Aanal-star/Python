import random
n = random.randint(1,100)
a = -1
guesses = 0
while( a != n):
    guesses +=1
    a = int (input("Guess Number"))
    if(a > n):
        print("Lower number")
    else:
        print("Higher number")
print(f"Correct number {guesses} attempts")