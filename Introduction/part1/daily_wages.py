# Please write a program which asks for the hourly wage, hours worked, and the day of the week. The program should then print out the daily wages, which equal hourly wage multiplied by hours worked, except on Sundays when the hourly wage is doubled.

#Sample output: 

#ourly wage: 8.5
#Hours worked: 3
#Day of the week: Monday
#Daily wages: 25.5 euros

#Hourly wage: 12.5
#Hours worked: 10
#Day of the week: Sunday
#Daily wages: 250.0 euros

#i check first if what the output if i times the hourly_wage into hours_worked which is the output is 25.5

#i check also what will happen if i double the multiply by 2 if the the day of week is sunday which is 250.0

# now that all checked i will then make an if else statement if == sunday it will double but if its not only the multiplied hourly_wag and hours_worked will print

# i have faced a problem FAIL: PythonEditorTest: test_sunday_1

#With input 25.0,15,Sunday correct wage 750.0 is not found in output Daily wages: 375.0 euros
#FAIL: PythonEditorTest: test_sunday_2

#With input 18.0,13,Sunday correct wage 468.0 is not found in output Daily wages: 234.0 euros

# my error is the == "sunday" needs to be capitalized == "Sunday"

# final working version

hourly_wage = float(input("Hourly wage:"))
hours_worked = int(input("Hours worked:"))
day_of_week = input("Day of the week:")

multiply = hourly_wage * hours_worked

if day_of_week == "Sunday":
    double = multiply * 2

    print(f"Daily wages: {double} euros")
else:
    print(f"Daily wages: {multiply} euros")