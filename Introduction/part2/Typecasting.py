#Please write a program which asks the user for a floating point number and then prints out the integer part and the decimal part separately. Use the Python int function.

#You can assume the number given by the user is always greater than zero.

#An example of expected behaviour:

#expected output 

#Please type in a number: 1.34
#Integer part: 1
#Decimal part: 0.34

#final working version
number = float(input("Please type in a number:"))

integer = int(number)

decimal = number - integer

print(f"Integer part:{integer}")
print(f"Decimal Part:{decimal}")

#Learned: Is i can use the in to transform the float number like round down 