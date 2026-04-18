#The function len can be used to find out the length of a string, among other things. The function returns the number of characters in a string.

#Some examples of how this works:

word = "abcd"
print(len(word))

print(len("hi there"))

word2 = "howdydoody"
length = len(word2)
print(length)

empty_string = ""
length = len(empty_string)
print(length)

#output:

#4
#8
#10
#0

# the problem is when i type a word i will use len to count the number of characters in the word

#word = input("Please type in a word: ")

#characters = len(word)

#print(f"There are {characters} letters in the word banana ")

#if characters < 1:
    #Thank you!
    
#final working version 
    
word = input("Please type in a word: ")

characters = len(word)

if characters <= 1:
    print("Thank you!")

else:
    print(f"There are {characters} letters in the word {word}")
    #forgot the thank you!
    print("Thank you!")

