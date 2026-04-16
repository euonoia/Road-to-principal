#Please write a program which asks the user for a temperature in degrees Fahrenheit, and then prints out the same in degrees Celsius. If the converted temperature falls below zero degrees Celsius, the program should also print out "Brr! It's cold in here!".

#The formula for converting degrees Fahrenheit to degrees Celsius can be found easily by any search engine of your choice.

#Two examples of expected behaviour:

#Please type in a temperature (F): 101
# 101 degrees Fahrenheit equals 38.333333333333336 degrees Celsius

#Please type in a temperature (F): 21
#21 degrees Fahrenheit equals -6.111111111111111 degrees Celsius
#Brr! It's cold in here!

#first i calculate the temperature in celsius by using the formula (F - 32) * 5 / 9. then i check if the temperature in celsius is below zero

#temp = int(input("Please type in a temperature(F):"))

#subtract = temp - 32 
#multiply = subtract * 5
#divide = multiply / 9

#print(f"{divide}")

#after initial testing i must now use the if else statement 

#this is my first attempt but when i say 32 degrees it doesnt print anything

#temp = int(input("Please type in a temperature(F):"))

#calculate the temperature(F)
#subtract = temp - 32 
#multiply = subtract * 5
#divide = multiply / 9
#Get the calculated degrees
#degrees = divide

#print(f"{degrees}")
#if degrees > 0:
    #print(f"{temp} degrees Fahrenheit equals {degrees} degrees Celcius")
#if degrees < 0:
    #print(f"{temp} degrees Fahrenheit equals {degrees} degrees Celcius")
    #print("Brr! it's cold in here!")

#it shows this error 2 != 1 : Your program printed out more than one row when input was 32
# and Your program did not print out message 'Brr! It's cold in here!' in a case where the temperature is below zero. Make sure that this print out happens with input 15

# the working version
temp = int(input("Please type in a temperature (F): "))

# Calculation (Simplified)
celsius = (temp - 32) * 5 / 9

# 1. Always print the conversion result
print(f"{temp} degrees Fahrenheit equals {celsius} degrees Celsius")

# 2. Separately check if it's below zero
if celsius < 0:
    print("Brr! It's cold in here!")