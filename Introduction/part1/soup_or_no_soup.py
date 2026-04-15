#Please write a program which asks for the user's name. If the name is anything but "Jerry", the program then asks for the number of portions and prints out the total cost. The price of a single portion is 5.90.

#expected output:

#Please tell me your name: Kramer
#How many portions of soup? 2
#The total cost is 11.8
#Next please!

#Please tell me your name: Jerry
#Next please!

#this is my first approach but it is not working as expected
#name = input("Please tell me your name: ")
#if the input is not equal to jerry we can proceed for taking the order
#if name == "jerry":
    #print("Next Please! ")
#but if the input is equal to jerry we need to skip him
#if name != "jerry":
    #portions = int(input("How many portions of soup? "))
    #cost = portions * 5.90 
    #print(f"The total cost is{cost}")
    #print("Next Please! ") 

#because what it want if i type kramer and jerry it will said next please

# this is the working version

name = input("Please tell me your name: ")

if name == "Jerry":
    # If the name is Jerry, we do nothing else and skip to the end
    print("Next please!")
else:
    # If the name is NOT Jerry, we ask for portions and calculate cost
    portions = int(input("How many portions of soup? "))
    total_cost = portions * 5.90
    print(f"The total cost is {total_cost}")
    print("Next please!")

#Learned: the if else statement of python is really do different from others