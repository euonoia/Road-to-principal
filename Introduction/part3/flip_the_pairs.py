#Please write a program which asks the user to type in a number. The program then prints out all the positive integer values from 1 up to the number. However, the order of the numbers is changed so that each pair or numbers is flipped. That is, 2 comes before 1, 4 before 3 and so forth. See the examples below for details.

#Sample output
#Please type in a number: 5
#2
#1
#4
#3
#5

#Sample output
#Please type in a number: 6
#2
#1
#4
#3
#6
#5

# Accept user input to define the upper limit of the sequence
number = int(input("Please type in a number: "))

# Initialize two pointers: 'i' for odd numbers, 'j' for even numbers
i = 1
j = 2

# Iterative loop to process sequences up to the user-defined limit
while i <= number:
    # Conditional check: Ensure the even number is within the range before printing
    if j <= number:
        print(j)
        j += 2 # Increment the even pointer
    
    # Process the odd number sequence
    print(i)
    i += 2 # Increment the odd pointer