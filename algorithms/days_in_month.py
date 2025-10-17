# Determine the number of days in a month
month = int(input())

if month < 1 or month > 12:
    print("Invalid month number")
elif month == 2:
    print(28)
elif month == 4 or month == 6 or month == 9 or month == 11:
    print(30)
else:
    print(31)