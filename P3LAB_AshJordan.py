# Jordan Ash

# 3/17/2024

# P3LAB

# Leap Year

year = int(input("Enter a year: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} - leap year")
else:
    print(f"{year} - not a leap year")
