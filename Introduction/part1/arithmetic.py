# the task here is to have an input of
#x = 27
#y = 15
#27 + 15 = 42
#27 - 15 = 12
#27 * 15 = 405
#27 / 15 = 1.8
# on my first attempt i printed out all the x and y variable to see that the print statement is working
x = 27
y = 15
# the problem is asking for the arithmetic solutions whereas i print the x and y based on the print statement i will give
#on what i have learned i can print increments without the ""
print(x + y)
print(x - y)
print(x * y)
print(x / y)
#what's is on my mind is i can use f string to make the 27 + 15  = 13 to come out
#this is the result of the code with f string
#print(f"{x} + {y} = " x + y)
#its not working and i found another solution
#instead of calculating inside the print statement i can make a variable that store the result
x = 27
y = 15

addition = (x + y)
print(f"{x} + {y} = {addition} ")
#this is my working approach so i am going to apply the same approach to the rest of the arithmetic operations

# Write your solution here
x = 27
y = 15

addition = (x + y)
print(f"{x} + {y} = {addition} ")

subtraction = (x - y)
print(f"{x} - {y} = {subtraction}")

multiplication = (x * y)
print(f"{x} * {y} = {multiplication}")

division = (x / y)
print(f"{x} / {y} = {division}")
# this is now the completed working version 
# Reflection: I am starting to be confident at my coding skills now without searching for answers