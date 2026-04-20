#Please write a program which asks the user for three letters. The program should then print out whichever of the three letters would be in the middle if the letters were in alphabetical order.

#You may assume the letters will be either all uppercase, or all lowercase.

#Some examples of expected behaviour:

#1st letter: x
#2nd letter: c
#3rd letter: p
#The letter in the middle is p

#1st letter: C
#2nd letter: B
#3rd letter: A
#The letter in the middle is B

#this problem uses the greater than and less than 

# 1. Get three letters from the user
first = input("1st letter: ")
second = input("2nd letter: ")
third = input("3rd letter: ")

# 2. Check if the 1st letter is the middle one.
# We check if it's between the others in normal order (second < first < third)
# OR in reverse order (third < first < second).
if (second < first < third) or (third < first < second):
    middle = first

# 3. If the 1st wasn't the middle, we check the 2nd letter.
# Again, we check both normal and reverse directions.
elif (first < second < third) or (third < second < first):
    middle = second

# 4. If neither the 1st nor the 2nd letter was the middle,
# then logically, the 3rd letter MUST be the middle one.
else:
    middle = third 

# 5. Print the final result using an f-string
print(f"The letter in the middle is {middle}")


