user_input = input("Greeting: ").strip().lower()
amount = 100
if user_input.startswith("hello"):
    amount = 0
elif user_input.startswith("h"):
    amount = 20

print(f"${amount}")