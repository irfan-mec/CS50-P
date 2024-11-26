from datetime import date, datetime
import sys
import inflect

p = inflect.engine()

def main():
    birth_date = input("Date of Birth (YYYY-MM-DD): ")
    try:
        birth = datetime.strptime(birth_date, "%Y-%m-%d").date()
        today = date.today()
        minutes = get_total_minutes(birth, today)
        print(f"{p.number_to_words(minutes, andword='').capitalize()} minutes")
    except ValueError:
        sys.exit("Invalid date")

def get_total_minutes(start_date, end_date):
    delta = end_date - start_date
    return round(delta.total_seconds() / 60)

if __name__ == "__main__":
    main()