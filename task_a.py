# Ask user for a day of the week
day = input("Enter a day of the week: ").strip().capitalize()

# Dictionary mapping days to numbers
days = {
    "Monday": 1,
    "Tuesday": 2,
    "Wednesday": 3,
    "Thursday": 4,
    "Friday": 5,
    "Saturday": 6,
    "Sunday": 7
}

# Check if the entered day is valid
if day in days:
    print(f"{day} is day {days[day]}")
else:
    print("Please enter a valid day")