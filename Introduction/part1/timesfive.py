#Task Please type in a number: 3 times 5 is 15
# we will use variable num = (input("please type in a number"))
# first approach i will try is this
# num = int(input("Please type in a number: ")) it prints the number into integer rather than string
# multiplication = (num * 5) this will multiply the number by 5
#print(f("{num} times 5 is {multiplication}")) this will print the result 
#expecting 3 times 5 is 15
# my error is (f("{num} times 5 is {multiplication}")) is not correct because it have to be print(f"{num} times 5 is {multiplication}") without the parentheses after the f
# this is the final working version of the code

num = int(input("Please type in a number: "))
multiplication = (num * 5)
print(f"{num} times 5 is {multiplication}")

# reflection: I am getting more comfortable with input and output in python i am happy to it