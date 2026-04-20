#Please write a program which asks the user for an integer number. If the number is divisible by three, the program should print out Fizz. If the number is divisible by five, the program should print out Buzz. If the number is divisible by both three and five, the program should print out FizzBuzz.

number = int(input("Number: "))

# 1. Check if divisible by both 3 AND 5 first
if number % 3 == 0 and number % 5 == 0:
    print("FizzBuzz")

# 2. If not both, check if divisible by 3
elif number % 3 == 0:
    print("Fizz")

# 3. If not 3, check if divisible by 5
elif number % 5 == 0:
    print("Buzz")
    
