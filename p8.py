# Inheritance

# When one class(child/derived) derives the properties & methods of another class
# (parent/base).

# Single Inheritance

# class Car:
#     color = "black"
#     @staticmethod
#     def start():
#         print("Car started....")

#     @staticmethod
#     def stop():
#         print("Car stop.")

# class ToyotaCar(Car):
#     def __init__(self, name):
#         self.name = name

# car1 = ToyotaCar("Fortuner")
# car2 = ToyotaCar("Prius")

# print(car1.name)
# print(car1.start())
# print(car1.color)


# Types of Inheritance
# 1) Single Inheritance  
# ----> Single Base and Single Derived Class

# 2) Multi-level Inheritance
# ---->  Base class -> Derived class -> Derived class

# 3) Multiple Inheritance
# ----> Base class 1 & Base class 2 -> Derived class


# Multi-level Inheritance

# class Car:
#     @staticmethod
#     def start():
#         print("Car started....")

#     @staticmethod
#     def stop():
#         print("Car stop.")

# class ToyotaCar(Car):
#     def __init__(self, brand):
#         self.name = brand

# class Fortuner(ToyotaCar):
#     def __init__(self, type):
#        self.type = type

# car1 = Fortuner("diesel")
# car1.start()


# Multiple Inheritance
class A:
    varA = "welcome to class A"

class B:
    varB = "welcome to class B"

class C(A, B):
    varC = "welcome to class C"

c1 = C()
print(c1.varC)
print(c1.varB)
print(c1.varA)
