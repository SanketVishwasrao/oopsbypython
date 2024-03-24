# Creating class
class Student: # class name starts with Capital letter

    # Default constructor
    def __init__(self):
        pass

    # Class attributes
    college_name = "ABC College"  # It is only stored once in memory

    # Parameterized Constructor
    def __init__(self, name, marks): # Contructor --> It always called every time per object called
        self.name = name  # Object attributes
        self.marks = marks
        # print("Adding new student in database")

    def welcome(self):
        print("welcome student", self.name)

    def get_marks(self):  
        return self.marks

# Creating object (instance)
s1 = Student("Sanket", 97) # s1 is the object of Student class. 
print(s1.name, s1.marks)

s2 = Student("Arjun", 88)
print(s2.name, s2.marks)
print(s2.college_name)

s1.welcome()
print(s1.get_marks())

# Constructor
# It is an __init__ function
# Attributes --> The data which is stored inside the class or object. It is also called variables

# Types of Attributes
# 1) Class Attribute
# 2) Instance Attribute --> self is the instance attribute

# Class is a collection of data(attributes) and methods(functions)

