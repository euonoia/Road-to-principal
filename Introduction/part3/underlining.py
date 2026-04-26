#Please write a program which asks the user for strings using a loop. The program prints out each string underlined as shown in the examples below. The execution ends when the user inputs an empty string - that is, just presses Enter at the prompt.

#Sample output
#Please type in a string: Hi there!

#Hi there!
#---------
#Please type in a string: This is a test

#This is a test
#--------------
#Please type in a string: a

#a
#-
#Please type in a string:

# Write your solution here

#i used boolean because i just need to loop please type in a string so if the lenght meets 0 it will stop the loop
while True:
    input_string = input("Please type in a string:")
    length = len(input_string)

    if length == 0:
        break

    print(input_string)
    print("-" * length)