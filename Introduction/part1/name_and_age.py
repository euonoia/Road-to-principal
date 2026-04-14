#Task: Please write a program which asks the user for their name and year of birth. The program then prints out a message as follows:
# What is your name? Frances Fictitious
#Which year were you born? 1990
#Hi Frances Fictitious, you will be 31 years old at the end of the year 2021

# Based on my observation and understanding the task tha name is string and the year born is int so i must use int(input(""))

# first approach i will try this

#name = input("What is your name? ")
#born = int(input("Which year were you born? "))

#i have noticed that it needs to be calculated to get the age so that the 31 years old will be printed out

#age = (2021 - born)

#i will use f string to print the result it will be like this
#print(f"Hi {name}, you will be {age} years old at the end of the year 2021")

# this is the final working version of the code

name = input("What is your name? ")
born = int(input("Which year were you born? "))
age = (2021 - born)
print(f"Hi {name}, you will be {age} years old at the end of the year 2021")

#reflection: I really love how my brain can now understand the logic of code and debugged it on my own.