# Ep20
# Constructors
# In python, a method with name __init()__ is a constructor.
#  This method is automatically called whrn an object is instantiated.

class ComplexNumber:
    def __init__(self, r = 0, i = 0): # constructor
        self.real = r
        self.imag = i

    def getData(self):
        print("{0}+{1}j".format(self.real, self.imag))

c1 = ComplexNumber(12, 34) # Create a new ComplexNumber object
c1.getData() # output: 12+34j

c2 = ComplexNumber() # Create a new ComplexNumber object
c2.getData() # output: 0+0j