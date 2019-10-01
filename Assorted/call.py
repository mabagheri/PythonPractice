"""
So, the __init__ method is used when the class is called to initialize the instance,
while the __call__ method is called when the instance is called –


Defining a custom __call__() method in the meta-class allows the class's instance to be called as a function,
not always modifying the instance itself.

"""
class Test:
    def __init__(self):
        print("init")

    def __call__(self):
        print("call ")

t = Test()
t()
