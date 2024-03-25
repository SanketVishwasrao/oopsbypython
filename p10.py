# Property decorator

# We use @property decorator on any method in the class to use the method as a property.

class Student:
    def __init__(self, phy, chem, maths):
        self.phy = phy
        self.chem = chem
        self.maths = maths

        # percentage
        # self.percentage = str((self.phy + self.chem + self.maths) / 3) + "%"

    # def calcPercentage(self):
    #     self.percentage = str((self.phy + self.chem + self.maths) / 3) + "%"
        
    @property
    def percentage(self):
        return str((self.phy + self.chem + self.maths) / 3) + "%"

stu1 = Student(98, 97, 99)
print(stu1.percentage)

# stu1.phy = 86
# print(stu1.phy)
# stu1.calcPercentage()
# print(stu1.percentage)

stu1.phy = 86
print(stu1.percentage)