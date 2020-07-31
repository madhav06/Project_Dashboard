# Inheritance
# Inheritance refers to defining a new class with little or no modification to an existing class.

class Mammal:
    def MammalFeatures(self):
        print("Mammal is a warm-blodded animal.")

# let's derive a new class "Dog" from this "Mammal" class.

class Mammal:
    def MammalFeatures(self):
        print("Mammal is a warm-blodded animal.")
class Dog(Mammal):
    def DogFeatures(self):
        print("Dog has 4 legs")

d = Dog()
d.DogFeatures()
d.MammalFeatures()