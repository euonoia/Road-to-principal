#Please write a program which asks the user for a number of days. The program then prints out the number of seconds in the amount of days given.
# How many days? 1
#Seconds in that many days: 86400
# since this is an integer we the int(input("")) to get the number of days and then we will multiply it by 24 hours and 60 minutes and 60 seconds to get the total number of seconds in that many days

# we will now calculate how many seconds in the number of days 

#this is my firs calculation seconds = ( days * 60 * 60)

#but that just computes as 1 so we will try

#sum = (days * 24) so it will calculate it as 24 hours in my mind

# this is the final working version of the code 
days = int(input("How many days? "))
sum = (days * 24)
seconds = ( sum * 60 * 60)
print(f"{days} day is {seconds} seconds")


