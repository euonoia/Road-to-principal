#the problem is asking to asks the user for two numbers. The program will then print out the sum and the product of the two numbers.

#expected output:

#Number 1: 3
#Number 2: 7
#The sum of the numbers: 10
#The product of the numbers: 21

#first approach i will try to use a augmented assignment operator 

#this is what in my mind number = 0 and then i will use number += int(input("Please type in the first number: ")) to add the number = 0 as 3 resulting as 0 + 3

#number = 0

#number += int(input("Number 1: "))
#number *= int(input("Number 2: "))

#print(f"The sum of {number}")

#but the problem is its only computing the product not the sum i am going to try a different approach

#this is my final working approach that i have applied

# first i need to make a variable that have an input function to ask the user for the first number and then i will make another variable that have an input function to ask the user for the second number 
number1 = int(input("Number 1: "))
number2 = int(input("Number 2: "))
# then i will calculate the sum and product of the two numbers by using the formula sum = (number1 + number2) and product = (number1 * number2)
sum = (number1 + number2)
product = (number1 * number2)
# then i will print the sum and product of the two numbers by using f string to compute this neatly and organized
print(f"The sum of the numbers: {sum}")
print(f"The product of the numbers: {product}")