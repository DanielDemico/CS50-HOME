vogals = ["a","e","i","o","u"]

def main():
    word = input("Input: ")
    shorten_word = shorten(word)
    print(shorten_word)


def shorten(word):
    new_str = ""
    for i in word:
        if not i in vogals:
            new_str += i
    return new_str

           
if __name__ == "__main__":
    main()