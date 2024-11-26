user_input = input("camelCase: ")
def camel_to_snake(string):
    result = []
    for letter in string:
      if letter.isupper():
          result.append("_")
      result.append(letter.lower())
    return "".join(result)
result = camel_to_snake(user_input)
print(f"snake_case: {result}")