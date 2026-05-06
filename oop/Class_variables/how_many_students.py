class Student:
    # Class Variables: Shared by the entire class
    class_year = 2024
    num_students = 0 # This acts as a global counter for the 'Student' type
    
    def __init__(self, name, age):
        # Instance Variables: Data specific to the individual
        self.name = name
        self.age = age
        
        # Automatic Tracking: Whenever a student is created, 
        # increment the class-level counter by 1.
        Student.num_students += 1

# Creating two separate instances
student1 = Student("SpongeBob", 30)
student2 = Student("Patrick", 35)

# The output now reflects the collective state of the class
print(f"my graduating class of {Student.class_year} has {Student.num_students} students")