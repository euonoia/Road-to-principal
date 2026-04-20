#Let's create a program along the lines of the example above. This program should print out the message "hi" and then ask "Shall we continue?" until the user inputs "no". Then the program should print out "okay then" and finish. Please have a look at the example below.

# this introduced the while loop

while True:
    decision = input("Shall we continue?")
    if decision == "no":
        break
    print("hi")

print("Okay Then")

#Reflection: as long as the decision is false it will always looping the hi and if the decision is true it will break 