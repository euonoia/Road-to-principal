#Please write a program which estimates a user's typical food expenditure.

#The program asks the user how many times a week they eat at the student cafeteria. Then it asks for the price of a typical student lunch, and for money spent on groceries during the week.

#Based on this information the program calculates the user's typical food expenditure both weekly and daily.

#The program should function as follows:

#How many times a week do you eat at the student cafeteria? 4
#The price of a typical student lunch? 2.5
#How much money do you spend on groceries in a week? 28.5

#Average food expenditure:
#Daily: 5.5 euros
#Weekly: 38.5 euros

#pseudocode: in a week he eats 4 times so 4 x 7 = 28 and then typical student lunch is 2.5 so 28.5 is the total of the food expenditure in a week and then we will divide it to 7 to get the daily expenditure

# this will be the input
#week = int(input("How many times a week do you eat at the student cafeteria? "))
#used a float because 2.5 is a decimal number
#price = float(input("The price of a typical student lunch? "))
#spend = float(input("How much money do you spend on groceries in a week? "))

# this is the first step calculation that i did and it did not go well 

#daily = (week * 7 + price)
#times = (daily / 5.5)

#weekly = (times * 7)

#print("Average food Expenditure:")
#print(f"Daily: {times} euros")
#print(f"Weekly: {weekly} euros")

# the output is not correct so i will try to fix it and make it work

#How many times a week do you eat at the student cafeteria? 4
#The price of a typical student lunch? 2.5
#How much money do you spend on groceries in a week? 28.5
#Average food Expenditure:
#Daily: 5.545454545454546 euros
#Weekly: 38.81818181818182 euros

#I have given up after a few attempts to fix the code i tried to ask on gemini and it gave me this code which is the final working version of the code

week = int(input("How many times a week do you eat at the student cafeteria? "))
price = float(input("The price of a typical student lunch? "))
money = float(input("How much money do you spend on groceries in a week? "))

#total spent in a week
# (4 times * 2.5 euros) + 28.50 euros = 38.50 euros
weekly = (week * price) + money

#total spent daily
# 38.50 / 7 = 5.5
daily = weekly / 7

print("Average food Expenditure:")
print(f"Daily: {daily} euros")
print(f"Weekly: {weekly} euros")

#reflection: What i have learned from here when you are going to calculate the daily to weekly expenditure and on daily you must divide it to 7 to know your daily expenditure