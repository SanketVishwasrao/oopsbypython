# Static methods
# Method that don't use the self parameter (work at class level)

# Decorators => Decorators allow us to wrap another function in order
#               to extend the behaviour of the wrapped function, without
#               permanently modifying it

class Student:
    @staticmethod   # decorator
    def hello():
        print("hello")

s1 = Student()
s1.hello()