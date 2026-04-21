#Part 1
#Please write a program which keeps asking the user for words. If the user types in end, the program should print out the story the words formed, and finish.

#Sample output
#Please type in a word: Once
#Please type in a word: upon
#Please type in a word: a
#Please type in a word: time
#Please type in a word: there
#Please type in a word: was
#Please type in a word: a
#Please type in a word: girl
#Please type in a word: end
#Once upon a time there was a girl

#Part 2
#Change the program so that the loop ends also if the user types in the same word twice in a row.

#Sample output
#Please type in a word: It
#Please type in a word: was
#Please type in a word: a
#Please type in a word: dark
#Please type in a word: and
#Please type in a word: stormy
#Please type in a word: night
#Please type in a word: night
#It was a dark and stormy night

# this is my final working code

iteration = ""
last_word = ""
while True:
    word = input("Please type in a word:")   
    if word == "end":
        break
    if word == last_word:
        break
    last_word = word
    iteration += word + " "
    
print(iteration)

#reflection: if i want to add some word together with the existing word i should use += but if only store i will use =