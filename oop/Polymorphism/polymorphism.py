from abc import ABC, abstractmethod

# THE CONTRACT (Abstraction)
class Shape(ABC): 
    @abstractmethod
    def area(self):
        pass

# CONCRETE IMPLEMENTATION 1
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        # Using the formula for a circle: πr²
        return 3.14 * self.radius ** 2
    
# CONCRETE IMPLEMENTATION 2
class Square(Shape):
    def __init__(self, side): 
        self.side = side
    def area(self):
        # Formula: side²
        return self.side ** 2
    
# CONCRETE IMPLEMENTATION 3
class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height
    def area(self):
        # Formula: ½ * base * height
        return self.base * self.height * 0.5
    
# MULTI-LEVEL INHERITANCE
class Pizza(Circle):
    def __init__(self, topping, radius):
        # super() calls the Circle's __init__ to handle the radius logic
        super().__init__(radius)
        self.topping = topping
    
# POLYMORPHISM IN ACTION
# We have a list containing 4 different objects, but we treat them all as "Shapes"
shapes = [Circle(4), Square(5), Triangle(6,7), Pizza("Pepperoni", 15)]

for s in shapes:
    # Polymorphism: Python knows which 'area' method to call based on the object type
    print(f"The area of the {type(s).__name__} is: {s.area()}")