def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):

    if not s[:2].isalpha():
        return False


    if not (2 <= len(s) <= 6):
        return False


    has_number = False
    for i, char in enumerate(s):
        if char.isdigit():

            if char == '0' and not has_number:
                return False
            has_number = True
        elif has_number:
            return False
    if not s.isalnum():
        return False

    return True


main()