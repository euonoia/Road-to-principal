class Pet:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def speak(self):
        print(f"Hello! I am {self.species} named {self.name}")

pet_name = Pet("Luna","Cat")

pet_name.speak()