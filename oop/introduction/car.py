# Define the class 'Car' - this is the template for all car objects
class Car:
    # The __init__ method is the 'Constructor'
    # It runs automatically the moment you create a new car
    def __init__(self, model, year, color, for_sale):
        # 'self' allows the object to store its own unique data
        self.model = model        # Assigns the model name to the object
        self.year = year          # Assigns the manufacturing year
        self.color = color        # Assigns the exterior color
        self.for_sale = for_sale  # Assigns the sale status (True/False)

    # A 'Method' defining the behavior of driving
    def drive(self):
        # We use self.attribute to pull the specific data for THIS car
        print(f"You drive the car {self.year} {self.color} {self.model}")
    
    # A 'Method' defining the behavior of stopping
    def stop(self):
        print(f"You stopped the car {self.year} {self.color} {self.model}")