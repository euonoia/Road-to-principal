#Please write a program which asks the user for a number. The program then prints out all integer numbers greater than zero but smaller than the input.

upper = int(input("Upper limit:"))
number = 1
#if number is less than upper it will stop
while number < upper:
    print(number)
    number += 1