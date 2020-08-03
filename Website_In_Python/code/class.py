# Ep12
# Object is simply a collection of variables and functions, that act on data.
# and class is blueprint for the object.

class Class_One:
    a = 100
    def func(self):
        print("function inside.")

# Once we define class, a new class object is created with same name. 
# this class object allows us to access the different attributes as well as 
# to instantiate new objects of that class.

print(Class_One.a) # output = 100
print(Class_One.func)

# visit this link to know more: https://medium.com/quick-code/understanding-self-in-python-a3704319e5f0

# creating objects

class Class_Two:
    a = 102
    def func_new(self):
        print("Welcome to classes and objects")
    
obj1 = Class_Two()
print(obj1.a)    # output: 102

obj2 = Class_Two()
print(obj1.a + 8)    # output: 110
