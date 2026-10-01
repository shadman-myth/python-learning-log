months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]
while True:
    date = input("Date:").strip()

    try:
        # Case 1: Numeric format like "9/8/1636"
        if "/" in date:
            month, day, year = date.split("/")
            month = int(month)
            day = int(day)
            year = int(year)
            if month < 1 or month > 12:
                raise ValueError
            if day < 1 or day > 31:
                raise ValueError
            print(f"{year:04}-{month:02}-{day:02}")
            break
        # Case 2: Textual format like "September 8, 1636"
        elif "," in date:
            month_day, year = date.split(", ")
            month, day = month_day.split(" ")
            month = month.strip()
            day = day.strip()
            year = year.strip()
            if month not in months:
                continue
            month_index = months.index(month) + 1
            day = int(day)
            year = int(year)
            if day < 1 or day > 31:
                raise ValueError
            if year < 1:
                raise ValueError
            print(f"{year:04}-{month_index:02}-{day:02}")
            break
        else:
            continue
    except ValueError:
        continue