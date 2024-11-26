grocery_list = {}

while True:
    try:
        item = input("").lower()
        if not item:
            break
        if item in grocery_list:
            grocery_list[item] += 1
        else:
            grocery_list[item] = 1
    except EOFError:
        break

sorted_list = dict(sorted(grocery_list.items()))

for item, count in sorted_list.items():
    print(f"{count} {item.upper()}")