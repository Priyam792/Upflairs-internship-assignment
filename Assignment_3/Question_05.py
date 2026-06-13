# Create a class named Circle with an attribute radius.             
# Create a method that calculates and prints the area of the circle.

#Solution -->
from math import pi
class Circle :
    def __init__(self,radius):
        self.radius = radius
    
    def area(self):
        print(f"The area of the circle is {2*pi*self.radius}")

a = int(input("Enter radius : "))
c = Circle(a)
c.area()