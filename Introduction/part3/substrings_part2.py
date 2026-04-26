#Please write a program which asks the user to type in a string. The program then prints out all the substrings which end with the last character, from the shortest to the longest. Have a look at the example below.

#Sample output
#Please type in a string: test
#t
#st
#est
#test

# Suffix Reveal Pattern: Prints substrings from the last character back to the full string
input_string = input("Please type in a string: ")

# Store the total length to calculate the starting point
length = len(input_string)

# Start the index at the last character (length - 1)
# This is the "Dynamic Variable" that will crawl backward
index = length - 1

# Loop runs until the index hits 0 (the beginning of the string)
while index >= 0:
    # Slice from the current index to the very end of the string
    print(input_string[index:])
    
    # Move the starting point one step to the left
    index -= 1