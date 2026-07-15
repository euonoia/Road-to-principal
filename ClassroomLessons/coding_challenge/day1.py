name = input("What is your name?: ")
favorite_number = int(input("What is your favorite number?: "))
is_like = input("Do you like coffee?: (yes/no) ").split().lower() == "yes"

print(f"HI! {name} your favorite number is {favorite_number} and  do you like ice cream? {is_like}")


