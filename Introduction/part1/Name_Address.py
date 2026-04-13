#Task: write a python program that asks the user for their name, address, city and postal code and then prints it out in a nice format.
#there is some error on here but i will try to fix it and make it work
name = input("What is your Given name? ")
family_name = input(" What is your family name? ")
street = input("What is your address? ")
City_and_postal  = input("What is your City and postal Code? ")
print(name + family_name)
print(street)
print(City_and_postal)
#what i have been missing is the " " between the name and family name and also i have to add a space before the question in the input function to make it look better. I have fixed it and now it works fine.
#this is the final corrected version

name = input("What is your name? ")
family_name = input("What is your family name? ")
street = input("what is your address? ")
City_and_postal = input("What is your City and postal Code? ")

print(name+" "+family_name)
print(street)
print(City_and_postal)

#this feels intimidating at first as the logic came i can now understand how to use the input function to get user input and how to concatenate strings using the + sign. I also learned that i have to pay attention to the details and check my code for any mistakes before running it. Overall, this was a good learning experience for me.