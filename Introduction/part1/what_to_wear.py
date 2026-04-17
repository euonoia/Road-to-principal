# Please write a program which asks for tomorrow's weather forecast and then suggests weather-appropriate clothing.

# The suggestion should change if the temperature (measured in degrees Celsius) is over 20, 10 or 5 degrees, and also if there is rain on the radar.

# Some examples of expected behaviour:

#What is the weather forecast for tomorrow?
#Temperature: 21
#Will it rain (yes/no): no
#Wear jeans and a T-shirt

#What is the weather forecast for tomorrow?
#Temperature: 11
#Will it rain (yes/no): no
#Wear jeans and a T-shirt
#I recommend a jumper as well

#What is the weather forecast for tomorrow?
#Temperature: 7
#Will it rain (yes/no): no
#Wear jeans and a T-shirt
#I recommend a jumper as well
#Take a jacket with you

#What is the weather forecast for tomorrow?
#Temperature: 3
#Will it rain (yes/no): yes
#Wear jeans and a T-shirt
#I recommend a jumper as well
#Take a jacket with you
#Make it a warm coat, actually
#I think gloves are in order
#Don't forget your umbrella!

# Write your solution here

print("What is the weather forecast for tomorrow?")
temperature = int(input("Temperature: "))
condition = input("Wil it rain (yes/no))")

#first i started into greater number to print the word if the condition is no
if temperature > 20:
    print("Wear jeans and a T-shirt")
elif temperature >= 15:
    print("Wear jeans and a T-shirt")
    print("I recommend a jumper as well")
elif temperature >= 10:
    print("Wear jeans and a T-shirt")
    print("Take a jacket with you")
    print("I recommend a jumper as well")
elif temperature >= 5:
    print("Wear jeans and a T-shirt")
    print("Take a jacket with you")
    print("Make it a warm coat, actually")
    print("I think gloves are in order") 
elif temperature >= 0:
    print("Wear jeans and a T-shirt")
    print("I recommend a jumper as well")
    print("Take a jacket with you")
    print("Make it a warm coat, actually")
    print("I think gloves are in order") 

#and if the condition is yes i used nested if statement so that when the temperature is below 10 degrees it will print out the recommend a jumper as well and umbrella and if the temperature is higher that 10 it will just say dont forget your umbrella
if condition == "yes":
    if temperature <= 10: 
        print("I recommend a jumper as well")
        print("Don't forget your umbrella!")
    elif temperature >= 10:
        print("Don't forget your umbrella!")
        
#what i have learned: the if condition can be nested so that if the condition is true it can make another condition inside that if condition its fascinating to me