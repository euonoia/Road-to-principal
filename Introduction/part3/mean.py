#Please write a function named mean, which takes three integer arguments. The function should print out the arithmetic mean of the three arguments.

#mean(5, 3, 1)
#mean(10, 1, 1)

#Sample output
#3.0
#4.0

# Write your code here

def mean(x, y, z):
    """
    Calculates and prints the arithmetic mean of three provided integers/floats.
    x, y, z: Numerical inputs (parameters)
    """
    # Summation: Aggregate the inputs
    addition = x + y + z
    
    # Calculation: Divide the sum by the count of elements
    division = addition / 3
    
    # Output: Display the resulting average
    print(division)

# Testing the function
# This block demonstrates a functional test case with known values
if __name__ == "__main__":
    mean(1, 2, 3)