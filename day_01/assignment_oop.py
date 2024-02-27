""" Task 1 

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def show(self):
        print(f'Name is {self.name} and age is {self.age}')

arpan = Person('Arpan', 23) 

arpan.show()
"""


"""Task 2

import math

class Circle:

    def __init__(self):
        self.radius = None
    
    def get_radius(self):
        return self.radius

    def set_radius(self, radius):
        self.radius = radius
    
    def getArea(self):
        area = math.pi * self.radius ** 2 
        print(f'Area of circle is {area}')

    def getCircimference(self):
        circumference = 2 * math.pi * self.radius
        print(f'Circumference is {circumference}')

new_circle = Circle()
new_circle.set_radius(3)
print(new_circle.get_radius())
print(new_circle.getArea())
print(new_circle.getCircimference())

"""

