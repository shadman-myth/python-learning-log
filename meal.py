def convert(time):
    hours, minutes = time.split(":")
    hours = int(hours)
    minutes = int(minutes)
    return hours + minutes / 60

def main():
    time = input("What time is it? ")
    converted = convert(time)
    if 7 <= converted <= 8:
        print("breakfast time")
    elif 12 <= converted <= 13:
        print("lunch time")
    elif 18 <= converted <= 19:
        print("dinner time")

if __name__ == "__main__":
    main()