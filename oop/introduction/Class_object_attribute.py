# Import the 'Car' class definition from the 'car' module
from car import Car

# Instantiate a Car object with specific attributes (Make, Year, Color, Luxury status)
# This creates a unique 'instance' of the Car class in memory
car1 = Car("Lamborghini", 2021, "red", False)

# Invoke the 'drive' method to execute the object's specific behavior
car1.drive()