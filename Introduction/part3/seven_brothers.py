#Please write a function named seven_brothers. When the function is called, it should print out the names of the seven brothers in alphabetical order, as in the example below. See the similarly named exercise in part 1 for more details about the brothers.

#Aapo
#Eero
#Juhani
#Lauri
#Simeoni
#Timo
#Tuomas

# Write your solution here

def seven_brothers():
    """
    Prints the names of the seven brothers in alphabetical order.
    This function encapsulates the output logic for easy reuse.
    """
    print("Aapo")   
    print("Eero")
    print("Juhani")
    print("Lauri")
    print("Simeoni")
    print("Timo")
    print("Tuomas")
    
# The boilerplate below ensures the function only runs if the script 
# is executed directly, not when imported as a module in another file.
if __name__ == "__main__":
    seven_brothers()
