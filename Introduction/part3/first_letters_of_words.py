#Please write a program which asks the user to type in a sentence. The program then prints out the first letter of each word in the sentence, each letter on a separate line.

#An example of expected behaviour:

#Sample output
#Please type in a sentence: #umpty Dumpty sat on a wall
#H
#D
#s
#o
#a
#w

# Capture the input string for processing
sentence = input("Please type in a sentence:")

# Print the initial character (the start of the first word)
print(sentence[0])

# Initialize the counter to the second character index
i = 1

# Iterate through the string to identify subsequent word starts
while i < len(sentence):
    # Logic: If the preceding character is a whitespace, 
    # the current character is the beginning of a new word.
    if sentence[i-1] == " ":
        print(sentence[i])
    
    # Increment the pointer to continue traversal
    i += 1