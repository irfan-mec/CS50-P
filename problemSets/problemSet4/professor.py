import random

def main():
    level = get_level()
    score = 0

    for _ in range(10):
        x = generate_integer(level)
        y = generate_integer(level)
        correct_answer = x + y
        attempts = 0

        while attempts < 3:
            user_answer = get_user_input(f"{x} + {y} = ")

            if user_answer is None:
                print("EEE")
                attempts += 1
            elif user_answer == correct_answer:
                score += 1
                break
            else:
                print("EEE")
                attempts += 1

        if attempts == 3:
            # Display the correct answer if the user fails to answer correctly within 3 attempts
            print(f"{x} + {y} = {correct_answer}")

    print(score)  # Only the number of correct answers

def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level in [1, 2, 3]:
                return level
            else:
                print("Invalid level. Please enter 1, 2, or 3.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def generate_integer(level):
    if level == 1:
        return random.randint(0, 9)
    elif level == 2:
        return random.randint(10, 99)
    elif level == 3:
        return random.randint(100, 999)
    else:
        raise ValueError("Invalid level")

def get_user_input(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a number.")

if __name__ == "__main__":
    main()
