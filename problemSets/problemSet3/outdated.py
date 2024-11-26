months = [
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"
]

while True:
    user_date = input("Date: ").strip()

    try:
        month, day, year = user_date.split("/")
        month = int(month)
        day = int(day)
        year = int(year)

        if 1 <= month <= 12 and 1 <= day <= 31 and len(str(year)) == 4:
            formatted_date = f"{year:04d}-{month:02d}-{day:02d}"
            print(formatted_date)
            break

    except ValueError:
        try:
            month_name, remaining = user_date.split(" ", 1)
            if month_name.title() in months:
                month = months.index(month_name.title()) + 1
                day, year = remaining.split(",")
                day = int(day.strip())
                year = int(year.strip())

                if 1 <= month <= 12 and 1 <= day <= 31 and len(str(year)) == 4:
                    formatted_date = f"{year:04d}-{month:02d}-{day:02d}"
                    print(formatted_date)
                    break
        except (ValueError, IndexError):
            pass