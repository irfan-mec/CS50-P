import re

def main():
    print(count(input("Text: ")))

def count(s):
    # Use regular expression to find "um" as a standalone word (case-insensitive)
    return len(re.findall(r'\bum\b', s, re.IGNORECASE))

if __name__ == "__main__":
    main()