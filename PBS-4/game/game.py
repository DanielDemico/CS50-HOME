import random

while True:
    try:
        n = int(input("Level: "))
        break
    except ValueError:
        continue

target = random.randint(1,n)

while True:
    try:
        g = int(input("Guess: "))
    except ValueError:
        continue
    if g == target:
        print("just right!")
        break
    elif g > target:
        print("Too large!")
        continue
    elif g < target:
        print("Too Small!")
        continue
    else:
        print("Something Wrong")
        break

    

    