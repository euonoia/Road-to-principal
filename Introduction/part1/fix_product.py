#This program asks the user for three numbers. The program then prints out their product, that is, the numbers multiplied by each other. There is, however, something wrong with the program - it doesn't work quite right, as you can see if you run it. Please fix it.
#number = int(input("Please type in the first number: "))
#number = int(input("Please type in the second number: "))
#number = int(input("Please type in the third number: "))
#product = number * number * number
#print("The product is", product)
# the problem on here is the output is 125 not 30
# first approach i will try is to += to the variable number so it will add the input to the variable number instead of overwriting it
# this is the example number += int(input("Please type in the first number: "))
# I have tried to put the sum = 0 and worsen the code so it will be like this
# i removed the + = 
# changes the product = number * number * number to product = number + number * number the plus sign 
# i tried doing it on + but the output is 9 on my 1 2 3 input

# i have removed the product = number * number * number 

# what i have done is i put a variable number = 0 and then i change the first input as number += int(input("Please type in the first number: ")) to add the number = 0 as 1 resulting as 0 + 1
# and then we will compute the second number but this time its multiplication number *= int(input("Please type in the second number: ")) to add the number 1 as 1 * 2 resulting as 1 x 2
# and lastly we will compute the third number but this time its multiplication number *= int(input("Please type in the third number: ")) to add the number 2 as 2 * 3 resulting as 2 x 3 
# and then i used f string to compute this neatly and organized and i will get the variable number = 0 to compute the already calculated using the augmented assignment operators (+= and *=),

# this is the final working version of the code

number = 0;

number += int(input("Please type in the first number: "))
number *= int(input("Please type in the second number: "))
number *= int(input("Please type in the third number: "))

print(f"The product is {number}")




