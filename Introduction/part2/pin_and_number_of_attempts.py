#Please write a program which keeps asking the user for a PIN code until they type in the correct one, which is 4321. The program should then print out the number of times the user tried different codes.

#PIN: 3245
#Wrong
#PIN: 1234
#Wrong
#PIN: 0000
#Wrong
#PIN: 4321
#Correct! It took you 4 attempts

#If the user gets it right on the first try, the program should print out something a bit different:

#PIN: 4321
#Correct! It only took you one single attempt!

attempts = 0

while True:
    pin = int(input("Pin:"))
    #this will increment the attempts
    attempts += 1
    if pin == 4321:
        break
    print("Wrong")
#will check if the attempts is equal to 1 to print the single attempt but if its not it will print the Correct! it took you too many attempts
if attempts == 1:
    print("Correct! It only took you one single attempt!")
else:
    print(f"Correct! It took you {attempts} attempts")

#reflection: I had to use the while loop to keep asking the user for the pin until they get it right and it will print the single attempt and too many attempts I am getting better at this