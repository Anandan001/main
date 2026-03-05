import calendar

# Get user input for the year and month
year = int(input("Enter the year (e.g., 2025): "))
month = int(input("Enter the month (1-12): "))

# Print the calendar for the specified month and year
print(calendar.month(year, month))
print(calendar.calendar(year))
