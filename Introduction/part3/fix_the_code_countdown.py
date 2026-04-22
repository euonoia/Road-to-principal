#The program below has some syntactic issues:

#print("Are you ready?")
#number = int(input("Please type in a number: "))
#while number = 0:
#print(number)
#print("Now!")
#Please fix it so that it prints out the following:

#Sample output
#Are you ready?
#Please type in a number: 5
#5
#4
#3
#2
#1
#Now!

#This exercise is similar to the countdown exercise in the last section, but please don't use a while True loop this time round!

# Fix the program
#print("Are you ready?")
#number = int(input("Please type in a number: "))
#while number = 0:
#print(number)
#print("Now!")

# Fix the program

print("Are you ready?")
number = int(input("Please type in a number: "))
#I initialized a variable 1 
countdown = 1
#the condition is if the number greater than equal to countdown
while number >= countdown:
    print(number)
    #it will decrement until the countdown meet 
    number -= 1
#will print if the condition has meet
print("Now!")

