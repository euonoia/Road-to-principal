#Please write a program which finds the second occurrence of a substring. If there is no second (or first) occurrence, the program should print out a message accordingly.

#In this exercise the occurrences cannot overlap. For example, in the string aaaa the second occurrence of the substring aa is at index 2.

#Some examples of expected behaviour:

#Sample output
#Please type in a string: abcabc
#Please type in a substring: ab
#The second occurrence of the substring is at index 3.

#Sample output
#Please type in a string: methodology
#Please type in a substring: o
#The second occurrence of the substring is at index 6.

#Sample output
#Please type in a string: aybabtu
#Please type in a substring: ba
#The substring does not occur twice in the string.

# Write your solution here

string = input("Please type in a string:")
substring = input("Please type in a substring")

# Identify the first occurrence of the substring
start_index = string.find(substring)

# Calculate the offset to begin the second search, ensuring no overlap with the first find
index2 = start_index + len(substring)

# Search for the next occurrence starting from the calculated offset
index3 = string.find(substring, index2)

# Multi-stage validation: First check if the substring exists at all
if start_index != -1:
    # Secondary check to confirm a repeat occurrence exists within the remaining string
    if index3 != -1:
        print(f"The second occurrence of the substring is at index {index3}.")
    else:
        # Fallback for single-occurrence scenarios
        print("The substring does not occur twice in the string.")
else:
    # Fallback for zero-occurrence scenarios
    print(f"The substring does not occur twice in the string.")