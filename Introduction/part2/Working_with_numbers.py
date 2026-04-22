#Pre-task

#Please write a program which asks the user for integer numbers. The program should keep asking for numbers until the user types in zero.

#Please type in integer numbers. Type in 0 to finish.
#Number: 5
#Number: 22
#Number: 9
#Number: -2
#Number: 0

#Part 2: Sum

#The program should also print out the sum of all the numbers typed in. The zero at the end should not be included in the calculation.

#The program should now print out the following:

#Sample output
#... the program asks for numbers
#Numbers typed in 4
#The sum of the numbers is 34

#Part 3: Mean
#The program should also print out the mean of the numbers. The zero at the end should not be included in the calculation. You may assume the user will always type in at least one valid non-zero number.

#Sample output
#... the program asks for numbers
#Numbers typed in 4
#The sum of the numbers is 34
#The mean of the numbers is 8.5

#Part 4: Positives and negatives
#The program should also print out statistics on how many of the numbers were positive and how many were negative. The zero at the end should not be included in the calculation.

#Sample output
#... the program asks for numbers
#Numbers typed in 4
#The sum of the numbers is 34
#The mean of the numbers is 8.5
#Positive numbers 3
#Negative numbers 1


integers = 0
typed = 0
positive = 0
negative = 0

while True:

    numbers = int(input("Please type in integer number. Type in 0 to finish"))
    # checks if certain conditions where meet if numbers is 0 it will stop and only increments if the numbers is greater or less than 0
    if numbers == 0:
        break
    elif numbers > 0:
        positive += 1
    elif numbers < 0:
        negative += 1
    # will increment on how many numbers i typed and will be totaling the sum of all numbers
    typed += 1
    integers += numbers
    
mean = integers / typed

print(f"Numbers typed in {typed}")
print(f"The sum of the numbers is {integers}")
print(f"The mean of the numbers is {mean}")
print(f"Positive numbers {positive}")
print(f"Negative numbers {negative}")