import re

def main():
    print(convert(input("Hours: ")))

def convert(s):
    # Regular expression to match the four time formats
    pattern = r"(\d{1,2}:\d{2}|\d{1,2}) (AM|PM) to (\d{1,2}:\d{2}|\d{1,2}) (AM|PM)"
    match = re.match(pattern, s)

    if not match:
        raise ValueError("Invalid format")

    # Extract the components
    start_time, start_period, end_time, end_period = match.groups()

    # Convert both start and end times to 24-hour format
    start_24 = convert_to_24_hour(start_time, start_period)
    end_24 = convert_to_24_hour(end_time, end_period)

    return f"{start_24} to {end_24}"

def convert_to_24_hour(time, period):
    # Split time into hour and minute, defaulting minute to 00 if it's not provided
    if ':' in time:
        hour, minute = map(int, time.split(':'))
    else:
        hour, minute = int(time), 0

    # Check for invalid hour or minute
    if hour > 12 or minute > 59:
        raise ValueError("Invalid time")

    # Convert to 24-hour format based on AM/PM
    if period == "AM":
        if hour == 12:  # 12 AM is midnight
            hour = 0
    elif period == "PM":
        if hour != 12:  # 12 PM is noon, no need to change
            hour += 12

    return f"{hour:02}:{minute:02}"

if __name__ == "__main__":
    main()