#Please write a program which asks the user for a string and then prints out a frame of * characters with the word in the centre. The width of the frame should be 30 characters. You may assume the input string will always fit inside the frame.

#If the length of the input string is an odd number, you may print out the word in either of the two possible centre locations.

#Sample output
#Word: testing

#******************************
#*          testing           *
#******************************
#Sample output
#Word: python

#******************************
#*           python           *
#******************************

# Write your solution here

input_string = input("Word:")

lenght = len(input_string)

line = 28

left_limit = (line - lenght) // 2
# this is the sauce for making both side is centered 
right_limit = line - lenght - left_limit

print("*" * 30)
print("*"+" " * left_limit + input_string + right_limit * " "+"*")
print("*" * 30)