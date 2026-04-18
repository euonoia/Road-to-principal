#Please write a program which asks for the names and ages of two persons. The program should then print out the name of the elder.

#Some examples of expected behaviour:

#Person 1:
#Name: Alan
#Age: 26
#Person 2:
#Name: Ada
#Age: 27
#The elder is Ada

#Person 1:
#Name: Bill
#Age: 1
#Person 2:
#Name: Jean
#Age: 1
#Bill and Jean are the same age

print("Person 1:")
name = input("Name:")
age = int(input("Age:"))

print("Person 2:")
name1 = input("Name:")
age1 = int(input("Age:"))

if age > age1:
    print(f"The elder is {name}")
elif age1 > age:
    print(f"The elder is {name1}")
else:
    print(f"{name} and {name1} are the same age")