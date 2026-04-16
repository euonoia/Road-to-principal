#Please write a program which asks the user for two numbers and an operation. If the operation is add, multiply or subtract, the program should calculate and print out the result of the operation with the given numbers. If the user types in anything else, the program should print out nothing.

#expected output:

#Number 1: 10
#Number 2: 17
#Operation: add

#10 + 17 = 27

#Number 1: 4
#Number 2: 6
#Operation: multiply

#4 * 6 = 24

#Number 1: 4
#Number 2: 6
#Operation: subtract

#4 - 6 = -2

# Write your solution here

number1 = int(input("Number 1: "))
number2 = int(input("Number 2: "))
operation = input("Operation: ")

if operation == "add":
    addition = number1 + number2
    print(f"{number1} + {number2} = {addition}")
if operation == "multiply":
    multiplication = number1 * number2
    print(f"{number1} * {number2} = {multiplication}")
if operation == "subtract":
    subtraction = number1 - number2
    print(f"{number1} - {number2} = {subtraction}")

# this is what i did: i first asked the user for the first number and then for the second number and then for the operation. then i used if statements to check which operation the user wanted to do and then i performed that operation and printed out the result. if the user typed in anything else than add, multiply or subtract then nothing would be printed out.