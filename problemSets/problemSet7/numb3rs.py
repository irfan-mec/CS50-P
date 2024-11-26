import re

def main():
    print(validate(input("IPv4 Address: ")))

def validate(ip):
    # Regular expression to match IPv4 addresses
    pattern = r"^([0-9]{1,3}\.){3}[0-9]{1,3}$"

    if re.match(pattern, ip):
        # Split the IP by '.' and check if each part is between 0 and 255
        parts = ip.split(".")
        for part in parts:
            if not 0 <= int(part) <= 255:
                return False
        return True
    return False

if __name__ == "__main__":
    main()