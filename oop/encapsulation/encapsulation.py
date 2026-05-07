class Computer:
    def __init__(self, maxprice):
        # The double underscore '__' makes this a PRIVATE attribute.
        # It cannot be changed directly from outside the class.
        self.__maxprice = maxprice
    
    def sell(self):
        # We can still access the private variable from WITHIN the class
        print(f"Selling Price: {self.__maxprice}")

    # This is called a 'Setter' method. It's the "official" way to 
    # change a private variable, often used to add validation logic later.
    def setMaxPrice(self, price):
        self.__maxprice = price

# 1. Create the object
comp1 = Computer(1000)
comp1.sell() # Output: 1000

# 2. Attempting to change a private variable directly
# This DOES NOT work. It actually creates a NEW variable called '__maxprice' 
# instead of changing the internal hidden one.
comp1.__maxprice = 1500 
comp1.sell() # Output: Still 1000 (The internal value stayed protected!)

# 3. Using the 'Setter' to change the price properly
comp1.setMaxPrice(100)
comp1.sell() # Output: 100