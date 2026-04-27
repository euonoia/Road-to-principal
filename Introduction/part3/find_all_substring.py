#Please make an extended version of the previous program, which prints out all the substrings which are at least three characters long, and which begin with the character specified by the user. You may assume the input string is at least three characters long.

#Sample output
#Please type in a word: mammoth
#Please type in a character: m
#mam
#mmo
#mot

#Sample output
#Please type in a word: banana
#Please type in a character: n
#nan

# Write your solution here
word = input("Please type in a word:")
characters = input("Please type in a character:")

# Initiate an iterative search to find all possible matches
while True:
    index = word.find(characters)
    
    # Termination Case 1: The search string has been fully processed
    if len(word) == 0:
        break
    
    # Termination Case 2: The target character is no longer present in the remaining string
    if index == -1:
        break
    
    # Validation Logic: Ensure the remaining substring length satisfies the 3-character requirement
    if index + 3 <= len(word):
        print(word[index:index + 3])

    # String Truncation: Advance the starting point past the current match to continue the search
    word = word[index + 1:]