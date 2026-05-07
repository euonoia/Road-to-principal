# The Parent Class (Superclass): Defines common traits for ALL animals
class Animals:
    def __init__(self, name):
        self.name = name
        self.is_alive = True
    
    def eat(self):
        # Every animal inherits this 'eat' behavior
        print(f"{self.name} is eating")
    
    def sleep(self):
        # Every animal inherits this 'sleep' behavior
        print(f"{self.name} is sleeping")

# The Child Classes (Subclasses): They inherit from 'Animals'
# but add their own unique 'speak' behaviors.
class Dog(Animals):
    def speak(self):
        print("woof")

class Cat(Animals):
    def speak(self):
        print("Meow")

class Mouse(Animals):
    def speak(self):
        print("squeek")

# Creating Instances
dog = Dog("Scooby")
cat = Cat("oggy")
mouse = Mouse("Jerry")

# Testing Inheritance: 
# 'mouse' doesn't have 'eat' or 'sleep' defined inside its own class,
# but it can use them because its Parent (Animals) has them.
mouse.eat()
mouse.sleep()

# Testing Unique Behavior:
mouse.speak()