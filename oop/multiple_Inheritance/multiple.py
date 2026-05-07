# Parent Class 1: Defines a specific "Role" or behavior
class Prey:
    def flee(self):
        print("This animal is fleeing")

# Parent Class 2: Defines a different "Role"
class Predator:
    def hunt(self):
        print("This animal is hunting")

# Single Inheritance: A Rabbit is only a Prey animal
class Rabbit(Prey):
    # 'pass' is used as a placeholder because the logic is already 
    # inherited from the parent; no new code is needed here.
    pass

# Single Inheritance: A Hawk is only a Predator
class Hawk(Predator):
    pass

# Multiple Inheritance: A Fish can be BOTH a Prey and a Predator
# It "mixes in" the methods from both parent classes.
class Fish(Prey, Predator):
    pass

# Instantiating the objects
rabbit = Rabbit()
hawk = Hawk()
fish = Fish()

# Testing Single Inheritance
rabbit.flee()

# Testing Multiple Inheritance
# The Fish object has access to the entire 'toolbox' of both parents
fish.hunt()
fish.flee()