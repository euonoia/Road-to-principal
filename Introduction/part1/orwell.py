#Please write a program which asks the user for an integer number. The program should print out "Orwell" if the number is exactly 1984, and otherwise do nothing.

#expected output:
#Please type in a number: 2020
#nothing prints

#Please type in a number: 1984
#Orwell

#first approach i will try to use an if statement its really different from others

number = int(input("please type in a number: "))

#now since we need to print orwell if we type 1984 we will use == is equal to operator to strictly compare the number to 1984 and if it is true we will print orwell if not it will do nothing

if number == 1984:
    print("Orwell")

print(" ")