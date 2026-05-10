import random

randoms = random.randint(55,60)

i = 0
while True:

    guess = int(input("Guess The number from 1 to 100: "))
	
    if guess == randoms:
        print("You Won!")
        break
    elif guess > randoms:
        print("Too High!")
    elif guess < randoms:
        print("Too low!")
    else:
        print("Thats not a number!")
    
    i += 1

print(f"Your number of guess {i}")