#Please write a program which asks the user for a string. The program then prints out the input string in reversed order, from end to beginning. Each character should be on a separate line.

#An example of expected behaviour:

#Sample output
#Please type in a string: hiya
#a
#y
#i
#h

input_string = input("Please type in a string:")
length = len(input_string) 
index = -1

#checks if the lenght is greater than equal to index
while index >= -length:
    #prints the input string by index
    print(input_string[index])
    #loops until the index matches the length
    index -= 1
