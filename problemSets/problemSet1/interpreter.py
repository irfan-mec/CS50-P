user_input = input("Expression: ").split(" ")
x = int(user_input[0])
y = user_input[1]
z = int(user_input[2])
result = 0
if y == '+':
    result = x+z
elif y == '-':
    result = x-z
elif y == '*':
    result = x*z
elif y == '/':
    if z!=0:
      result = x/z
    else:
      print("Cannot divide by zero")
      exit()
else:
    print("Invalid operation")
    exit()

print(float(round(result,1)))