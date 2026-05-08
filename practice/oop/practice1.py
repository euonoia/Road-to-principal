class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

        print(f"The dog name is {self.name} and his age is {self.age}")
    def bark(self):
        print(f"{self.name} barked at me")

    def human_age(self):
        return self.age * 7
my_dog = Dog("Lebron", 90)

my_dog.bark()
print(f"In Human years he is {my_dog.human_age()} years old")