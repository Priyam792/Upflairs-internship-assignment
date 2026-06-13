# Create a class named Rectangle with attributes: 
# o length  
# o width             
# Create a method to calculate and print the area of the rectangle

#Solution -->

class Rectangle :
    def __init__(self,length, width):
        self.length = length
        self.width = width
    def area(self):
        print(f"The area is {self.length*self.width}")

a = int(input("Enter your length : "))
b = int(input("Enter your width : "))
r = Rectangle(a,b)
r.area()
