from abc import ABC, abstractmethod

# The Abstract Base Class (ABC): This acts as a blueprint/template.
# You cannot create an object directly from 'Vehicle'.
class Vehicle(ABC):

    # Abstract Method: Defines a required behavior.
    # It has no body (pass) because the specifics depend on the child class.
    @abstractmethod
    def go(self):
        pass

    @abstractmethod
    def stop(self):
        pass

# The Concrete Class: This 'fills in the blanks' of the abstract blueprint.
class Car(Vehicle):
    # Implementation: If you forgot to write 'go' or 'stop' here, 
    # Python would throw an error immediately.
    def go(self):
        print("You drive the car")
        
    def stop(self):
        print("You stop")

# Instantiating the concrete class
vehicle = Car()

vehicle.go()
vehicle.stop()

