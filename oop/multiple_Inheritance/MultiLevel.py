# The Grandparent Class: Root of all biological behavior
class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"{self.name} is eating")

    def sleep(self):
        print(f"{self.name} is sleeping")

# The Parent Classes (Level 1): Defining ecological roles
class Prey(Animal):
    def flee(self):
        print(f"{self.name} is fleeing") # Using name from the grandparent!

class Predator(Animal):
    def hunt(self):
        print(f"{self.name} is hunting")

# The Child Classes (Level 2): Specific species
class Rabbit(Prey):
    pass

class Hawk(Predator):
    pass

# The "Hybrid" Class: Combining multiple roles
class Fish(Prey, Predator):
    pass

# Instances
rabbit = Rabbit("Bugs")
hawk = Hawk("Tony")
fish = Fish("Nemo")

# Testing the 'Role' behavior
rabbit.flee()
hawk.hunt()

# Testing the 'Hybrid' behavior (Accessing two parents)
fish.hunt()
fish.flee()

# Testing the 'Inherited' behavior (Accessing the grandparent)
rabbit.eat()
rabbit.sleep()