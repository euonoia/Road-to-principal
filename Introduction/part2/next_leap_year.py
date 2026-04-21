#Please write a program which asks the user for a year, and prints out the next leap year.

#Sample output
#Year: 2023
#The next leap year after 2023 is 2024

#If the user inputs a year which is a leap year (such as 2024), the program should print out the following leap year:

#Sample output
#Year: 2024
#The next leap year after 2024 is 2028

year = int(input("Year:"))

#increment the year by 1
next_year = year + 1

while True:
    #checks if the next year is divisible by 4 or 400 but not 100
    if (next_year % 4 == 0 and next_year % 100 != 0) or (next_year % 400 == 0):
    #prints out if the condition is meant
        print(f"The next leap year after {year} is {next_year}")
        break
    # increment by += 1 to meet the condition
    next_year += 1 