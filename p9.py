# Super method

# super() method is used to access methods of the parent class.

class Car:
    def __init__(self, type):
        self.type = type

    @staticmethod
    def start():
        print("car started....")

    @staticmethod
    def stop():
        print("car stopped.")

class ToyotaCar(Car):
    def __init__(self, name, type):
        super().__init__(type)
        self.name = name
        super().start()

car1 = ToyotaCar("Prius", "electric")
print(car1.type)


# class method
# A class method is bound to the class & receives the class as an implicit first argument.
# Note:- static method can't access or modify class state & generally for utility.

class Person:
    name = "anonymous"

    # def changeName(self, name):
    #     # self.name = name
    #     # OR
    #     self.__class__.name = name

    @classmethod
    def changeName(cls, name):
        cls.name = name

p1 = Person()
p1.changeName('Rahul K')
print(p1.name)
print(Person.name)


# Types of methods
# 1) static methods (cls and instance method arguments are not used)
# 2) class methods (cls as a first implicit argument)
# 3) instance methods (self as an argument)