import random

def main():
    level = get_level()
    number = random.randint(1, level)

    while True:
        guess = get_guess()
        if guess < number:
            print("Too small!")
        elif guess > number:
            print("Too large!")
        else:
            print("Just right!")
            break

def get_level():
    while True:
        try:
            level = int(input("Enter the level: "))
            if level > 0:
                return level
            else:
                print("Please enter a positive integer.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def get_guess():
    while True:
        try:
            guess = int(input("Guess the number: "))
            if guess > 0:
                return guess
            else:
                print("Please enter a positive integer.")
        except ValueError:
            print("Invalid input. Please enter a number.")

if __name__ == "__main__":
    main()