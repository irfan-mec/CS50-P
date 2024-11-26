'''def main():
    time=input("What time is it? ").split(":")
    res = convert(time)
    if res>=7 and res<=8:
        print("breakfast time")
    elif res>=12 and res<=13:
        print("lunch time")
    elif res>=18 and res<=19:
        print("dinner time")

def convert(time):
    hrs = time[0]
    mins = time[1]
    return int(hrs)+int(mins)/60


if __name__ == "__main__":
    main()
    '''


def main():
  time = input("What time is it? ")
  converted_time = convert(time)

  if 7 <= converted_time <= 8:
    print("breakfast time")
  elif 12 <= converted_time <= 13:
    print("lunch time")
  elif 18 <= converted_time <= 19:
    print("dinner time")

def convert(time):
  hours, minutes = map(int, time.split(":"))
  return hours + minutes / 60



if __name__ == "__main__":
  main()