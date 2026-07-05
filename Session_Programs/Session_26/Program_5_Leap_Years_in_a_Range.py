"""
Session 26 - Assignment 2, Program 5: Leap Years in a Range

Print every leap year between two given years.

Sample Output:
Enter start year: 2000
Enter end year: 2020
2000 2004 2008 2012 2016 2020

Try also: 2010, 2025 gives 2012 2016 2020 2024.
"""

# Assignment 5: Leap years in a range
start = int(input("Enter start year: "))
end = int(input("Enter end year: "))
for year in range(start, end + 1):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print(year, end=" ")
print()
