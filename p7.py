# del keyword
# Used to delete object properties or object itself.

# del s1.name
# del s1

class Student:
    def __init__(self, name):
        self.name = name

s1 = Student("Sanket")
print(s1.name)

# del s1.name
# print(s1.name)


# Private (like) attributes and methods
# Private attributes & methods are meant to be used only within the class
# and are not accessible outside the class.


class Account:
    def __init__(self, acc_no, acc_pass):
        self.acc_no = acc_no
        self.__acc_pass = acc_pass

    def reset_pass(self):
        print(self.__acc_pass)

acc1 = Account("12345", "abcde")
print(acc1.acc_no)
# print(acc1.__acc_pass)
print(acc1.reset_pass())

class Person:
    __name = "anonymous"

    def __hello(self):
        print("hello person!")

    def welcome(self):
        self.__hello()
    
p1 = Person()
# print(p1.__name)
# print(p1.__hello())

print(p1.welcome())
