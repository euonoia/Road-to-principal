# This program calculates the end of year bonus a customer receives on their loyalty card. The bonus is calculated with the following formula:

# If there are less than a hundred points on the card, the bonus is 10 %
# In any other case the bonus is 15 %

# expected output

#How many points are on your card? 55
#Your bonus is 10 %
#You now have 60.5 points

#But there is a problem with the program, so with some inputs it doesn't work quite right:

#How many points are on your card? 95
#Your bonus is 10 %
#Your bonus is 15 %
#You now have 120.175 points

# Please fix the program so that there is always either a 10 % or a 15 % bonus, but never both.

# Fix the program
points = int(input("How many points are on your card? "))
if points < 100:
    points *= 1.1
    print("Your bonus is 10 %")

if points >= 100:
    points *= 1.15
    print("Your bonus is 15 %")

print("You now have", points, "points")

# first approach is i will test the code

# this is the error 
#FAIL: PythonEditorTest: test_under_99

#With input 99 instead of two rows, your program did print out 3 rows

# Fix version
points = int(input("How many points are on your card? "))

if points < 100:
    points *= 1.1
    print("Your bonus is 10 %")

elif points >= 100:
    points *= 1.15
    print("Your bonus is 15 %")

print("You now have", points, "points")

# i have seen the error if there is both if statement it will always going to print the true we need to check for the true and if its false the elif will came