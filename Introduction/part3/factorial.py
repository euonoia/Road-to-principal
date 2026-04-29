#Please write a program which asks the user to type in an integer number. If the user types in a number equal to or below 0, the execution ends. Otherwise the program prints out the factorial of the number.

#The factorial of a number involves multiplying the number by all the positive integers smaller than itself. In other words, it is the product of all positive integers less than or equal to the number. For example, the factorial of 5 is 1 * 2 * 3 * 4 * 5 = 120.

#Some examples of expected behaviour:

#Sample output
#Please type in a number: 3
#The factorial of the number 3 is 6
#Please type in a number: 4
#The factorial of the number 4 is 24
#Please type in a number: -1
#Thanks and bye!

#Sample output
#Please type in a number: 1
#The factorial of the number 1 is 1
#Please type in a number: 0
#Thanks and bye!

# Write your solution here

# Outer loop: Maintains program execution until a termination condition is met
while True:
    number = int(input("Please type in a number: "))

    # Sentinel Value: Exit the program if the user enters a non-positive integer
    if number <= 0:
        break

    # Initialize accumulation variables
    i = 0
    stored = 1 # Identity element for multiplication
    
    # Inner loop: Calculates the factorial by iterative multiplication
    while i < number:
        i += 1
        stored *= i # Update the product 'stored' by the current factor 'i'

    # Display the result using f-string interpolation for clarity
    print(f"The factorial of the number {number} is {stored}")

# Final cleanup message
print("Thanks and bye!")