import random

print("===============>> Guess game started <<=================")

attempts = 0

try:
    d = int(input("Choose difficulty: 1 easy, 2 medium, 3 hard: "))
except ValueError:
    print("Please enter only 1, 2, or 3")
    exit()

if d == 1:
    secret = random.randint(1, 20)
elif d == 2:
    secret = random.randint(1, 50)
elif d == 3:
    secret = random.randint(1, 100)
else:
    print("Wrong difficulty choice")
    exit()

while True:
    try:
        guess = int(input("Enter your guess: "))
    except ValueError:
        print("Make sure to type numbers")
        continue

    attempts += 1

    if guess == secret:
        print(f"Correct! You found it in {attempts} attempts")
        break
    elif guess < secret:
        print("too low")
    else:
        print("too high")