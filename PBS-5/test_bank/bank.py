def main():
    greeting = input("Greeting: ")
    print(f"${value(greeting)}")


def value(greeting):
    list_ = greeting.lower().split(" ")
    first_val = list_[0]
    if list_[0] == "hello":
        return 0
    elif list_[0][0].startswith("h"):
        return 20
    else:
        return 100

if __name__ == "__main__":
    main()