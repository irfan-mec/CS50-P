while True:
    try:
        fraction = input("Fraction (format X/Y): ").strip()

        x, y = fraction.split("/")
        x = int(x)
        y = int(y)

        if y == 0:
            raise ZeroDivisionError("Denominator cannot be zero")
        if x > y:
            raise ValueError("Numerator cannot be greater than denominator")

        percentage = (x / y) * 100

        if percentage <= 1:
            print("E")
        elif percentage >= 99:
            print("F")
        else:
            print(f"{round(percentage)}%")

        break

    except (ValueError, ZeroDivisionError):
        pass