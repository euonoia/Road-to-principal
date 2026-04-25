#You are running a small digital shop. You need to write a program that helps a user "buy" items until they run out of money or choose to quit.


budget = 100

apple = 5
shield = 45
potion = 20

print(f"Apple: ${apple}")
print(f"Shield: ${shield}")
print(f"Potion: ${potion}")

while True:
    
    decision = input("What do you want to buy? ")
    
    if decision == "quit":
        break

    elif decision == "apple":
        if budget < apple:
            print("you dont have sufficient money!")
        else:
            budget -= apple
            
    elif decision == "shield":
        if budget < shield:
            print("you dont have sufficient money!")
        else:    
            budget -= shield
    
    elif decision == "potion":
        if budget < potion:
            print("you dont have sufficient money!")
        else:
            budget -= potion

    else:
        print("invalid choice")
        
    print(f"your budget now is {budget}")

print("thank you for buying!")
    