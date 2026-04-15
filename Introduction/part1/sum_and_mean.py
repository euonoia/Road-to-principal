#Please write a program which asks the user for four numbers. The program then prints out the sum and the mean of the numbers.

#expected output:

#Number 1: 2
#Number 2: 1
#Number 3: 6
#Number 4: 7
#The sum of the numbers is 16 and the mean is 4.0

#based on my understanding of the problem i need to sum all the numbers to show the sum and divide it to have the mean 4.0

#first i need to have a input function number1 = int(input("Number 1: "))

#this is valid but it will make me some time to insert each variables

#number1 = int(input("Number 1: "))
#number2 = int(input("Number 2: "))
#number3 = int(input("Number 3: "))
#number4 = int(input("Number 4: "))

#i need to find a optimal approach to solve this problem

#i have used the augmented assignment operator
number = 0
#this will add when the user input a number like 2 and this is the output 0 + 2
number += int(input("Number 1: "))
number += int(input("Number 2: "))
number += int(input("Number 3: "))
#when it reaches here it will be 16 because 0 + 2 + 1 + 6 = 16
number += int(input("Number 4: "))
# and then if that gets all the sum we will get the mean by dividing the number to 4
mean = (number / 4)
# after that we will get the variable number for the sum and the mean for the variable mean 
print(f"The sum of the numbers is {number} and the mean is {mean}")
# the output is The sum of the numbers is 16 and the mean is 4.0

#I am starting to loving coding as i can see the logic and how to use the augmented assignment operator to make my code more efficient and organized. I also learned that i can use f string to make my output more neat and organized. Overall, this was a good learning experience for me.