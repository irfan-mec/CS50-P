user_input = input("Input: ")
result = []
for letter in user_input:
    if letter not in ['a','e','i','o','u','A','E','I','O','U']:
        result.append(letter)
output = "".join(result)
print(f"Output: {output}")