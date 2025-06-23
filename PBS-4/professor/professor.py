import random


def main():
    level = get_level()

    points = 0 
    for i in range(10):
        x = generate_integer(level)
        y = generate_integer(level)
        target = x + y
        
        for i in range(3):
            user_answer = input(f"{x} + {y} = ")
            try: 
                user_answer = int(user_answer)
            except ValueError:
                pass
            if user_answer != target or ValueError:
                print("EEE")
            else:
                points += 1 
                break 
            if i + 1 == 3: 
                print(f"{x} + {y} = {target}")

    print("Score:", points)

def get_level():
    while True:
        try:
            level = int(input("Level: "))
            
            if level < 1 or level > 3:
                raise ValueError
            else:
                return level
        except ValueError:
            continue


def generate_integer(level):
    if level == 1:
        return random.randint(0,9)
    elif level == 2:
        return random.randint(10,99)
    elif level == 3:
        return random.randint(100,999)



if __name__ == "__main__":
    main()