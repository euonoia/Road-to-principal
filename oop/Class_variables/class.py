class Student:
    # Class Variable: Shared by ALL students. 
    # Every student in this school belongs to the same class year.
    class_year = 2024

    # The Constructor (Initialization)
    def __init__(self, name, age):
        # Instance Variables: Unique to each specific student.
        # SpongeBob and Patrick have different names and ages.
        self.name = name
        self.age = age

# Creating "Instances" of the Student class
student1 = Student("SpongeBob", 30)
student2 = Student("Patrick", 35)

# Accessing Instance Data (Specific to student1)
print(student1.name)
print(student1.age)

# Accessing Class Data (The same for everyone)
# Note how we use the Class name 'Student' instead of 'student1'
print(Student.class_year)