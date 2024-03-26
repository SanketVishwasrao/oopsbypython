# Polymorphism : Operator Overloading
# When the same operator is allowed to have different meaning according to the context.

# Dunder function ----> These functions starting with __ (double underscore)

# print(1 + 2)
# print(type(1))

# print("apna" + "college")  # concatenate
# print(type("apna"))

# print([1, 2, 3] + [4, 5, 6])  # merge
# print(type([1, 2, 3]))


# Without using Dunder function
# class Complex:
#     def __init__(self, real, img):
#         self.real = real
#         self.img = img

#     def showNumber(self):
#         print(self.real, "i +", self.img, "j")

#     def add(self, num2):
#         newReal = self.real + num2.real
#         newImg = self.img + num2.img
#         return Complex(newReal, newImg)
    
# num1 = Complex(1, 3)
# num1.showNumber()

# num2 = Complex(4, 6)
# num2.showNumber()
# num3 = num1.add(num2)
# num3.showNumber()


# With using Dunder function
class Complex:
    def __init__(self, real, img):
        self.real = real
        self.img = img

    def showNumber(self):
        print(self.real, "i +", self.img, "j")

    def __add__(self, num2):
        newReal = self.real + num2.real
        newImg = self.img + num2.img
        return Complex(newReal, newImg)
    
num1 = Complex(1, 3)
num1.showNumber()

num2 = Complex(4, 6)
num2.showNumber()

num3 = num1 + num2
num3.showNumber()