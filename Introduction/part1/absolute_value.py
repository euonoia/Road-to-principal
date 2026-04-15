#Please write a program which asks the user for an integer number. If the number is less than zero, the program should print out the number multiplied by -1. Otherwise the program prints out the number as is. Please have a look at the examples of expected behaviour below.

#expected output

#Please type in a number: -7
#The absolute value of this number is 7

#Please type in a number: 1
#The absolute value of this number is 1

#this is the working code
number = int(input("Please Type in a number: "))

#if the number is less than 0 it will print out the absolute number 

if number < 0:
    multiply = number * -1
    print(f"The absolute value of this number is {multiply}")

#if the number is more than 0 it will print out the absolute number
if number > 0:
    print(f"The absolute value of this number is {number}")

#i forgot if how about the 0 we will use == strict is equal to operator
if number == 0:
    print(f"The absolute value of this number is {number}")

#reflection: The if statement is really different from the javascript its just so simple and easy to understand