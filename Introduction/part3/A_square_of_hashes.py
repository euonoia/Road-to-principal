#Please write a function named hash_square(length), which takes an integer argument. The function prints out a square of hash characters, and the argument specifies the length of the side of the square.

#hash_square(3)
#print()
#hash_square(5)
#Sample output

###
###
###

#####
#####
#####
#####
#####

# Write your solution here

def hash_square(length):
    """
    Generates a square grid of hash characters based on the provided dimensions.
    length: The integer value representing both width and height.
    """
    # String Multiplication: Create a single row of the square efficiently
    hashed = "#" * length
    
    # Initialize row counter
    i = 1
    
    # Loop Logic: Iterate through each row until the 'length' count is reached
    while i <= length:
        print(hashed)
        # Increment to advance to the next row
        i += 1
        
    # Vertical spacing for clean output formatting
    print()

# Test block: Executes the function to generate a 5x5 hash grid
if __name__ == "__main__":
    hash_square(5)