#Please write a program which asks for two integer numbers. The program should then print out whichever is greater. If the numbers are equal, the program should print a different message.

#Some examples of expected behaviour:

#Sample output
#Please type in the first number: 5
#Please type in another number: 3
#The greater number was: 5

#Sample output
#Please type in the first number: 5
#Please type in another number: 8
#The greater number was: 8

#Sample output
#Please type in the first number: 5
#Please type in another number: 5
#The numbers are equal!

number = int(input("Please type in the first number:"))
number1 = int(input("Please type in another number:"))

if number > number1:
    print(f"The greater number was:{number}")
elif number1 > number:
    print(f"The greater number was:{number1}")
else:
    print("The numbers are equal")

#learned: i can use double > if i want to compare two numbers vice versa and if the output is false both it will print the else