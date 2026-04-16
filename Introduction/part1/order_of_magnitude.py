#Please write a program which asks the user for an integer number. The program should then print out the magnitude of the number according to the following examples.

#expected output:

#Please type in a number: 950
#This number is smaller than 1000
#Thank you!

#Please type in a number: 59
#This number is smaller than 1000
#This number is smaller than 100
#Thank you!

#Please type in a number: 2
#This number is smaller than 1000
#This number is smaller than 100
#This number is smaller than 10
#Thank you!

#Please type in a number: 1123
#Thank you!

#This is a working program
number = int(input("Please type in a number: "))

if number < 10:
    print("This number is smaller than 1000")
    print("This number is smaller than 100")
    print("This number is smaller than 10")
    print("Thank you!")
elif number < 100:
    print("This number is smaller than 1000")
    print("This number is smaller than 100")
    print("Thank you!")
elif number < 1000:
    print("This number is smaller than 1000")
    print("Thank you!")
else:
    print("Thank you!")

#reflection: if i am using a if else statement on magnitude of number i must start with the smallest magnitude and then move to the bigger one. if i start with the biggest magnitude then the smaller magnitude will never be reached.