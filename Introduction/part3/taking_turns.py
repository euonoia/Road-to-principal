#Please write a program which asks the user to type in a number. The program then prints out the positive integers between 1 and the number itself, alternating between the two ends of the range as in the examples below.

#Sample output
#Please type in a number: 5
#1
#5
#2
#4
#3

#Sample output
#Please type in a number: 6
#1
#6
#2
#5
#3
#4

# Write your solution here
number = int(input("Please type in a number: "))

# Initialize two pointers at opposite ends of the sequence
high = 1
low = number

# Execute the loop as long as the pointers have not crossed each other
while high <= low:
    # Print the current value from the start of the sequence
    print(high)
    
    # Conditional Check: Prevents duplicate printing of the middle number 
    # when 'high' and 'low' meet at the same index (odd-numbered inputs)
    if low != high:
        print(low)
    
    # Move pointers inward to process the next pair
    low -= 1
    high += 1