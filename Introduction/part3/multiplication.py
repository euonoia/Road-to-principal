#Please write a program which asks the user for a positive integer number. The program then prints out a list of multiplication operations until both operands reach the number given by the user. See the examples below for details:

#Sample output
#Please type in a number: 2
#1 x 1 = 1
#1 x 2 = 2
#2 x 1 = 2
#2 x 2 = 4

#Sample output
#Please type in a number: 3
#1 x 1 = 1
#1 x 2 = 2
#1 x 3 = 3
#2 x 1 = 2
#2 x 2 = 4
#2 x 3 = 6
#3 x 1 = 3
#3 x 2 = 6
#3 x 3 = 9

# Accept user input to define the boundary for the multiplication table
limit = int(input("Please type in a number:"))

# Initialize the outer loop counter
i = 1

# Outer Loop: Controls the primary factor (rows)
while i <= limit:
    # Initialize the inner loop counter for each new row
    j = 1
    
    # Inner Loop: Iterates through the secondary factor (columns) for the current row
    while j <= limit:
        # Execute the calculation and print formatted output
        print(f"{i} x {j} = {i*j}")
        
        # Increment the inner counter
        j += 1
        
    # Increment the outer counter after the inner loop completes its full cycle
    i += 1

