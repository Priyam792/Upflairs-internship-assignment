# Create a class named Calculator with methods: 
# o add()  
# o subtract()  
# o multiply()  
# o divide()           
# Take two numbers as input and perform all operations

#Solution -->

class Calculator :
    def __init__(self,num1,num2):
        self.num1 = num1
        self.num2 = num2
    
    def add(self):
        print(f"Addition : {self.num1 + self.num2}")
    def subtract(self):
        print(f"Subtraction : {self.num1 - self.num2}")
    def multiply(self):
        print(f"Multiplication : {self.num1 * self.num2}")
    def divide(self):
        print(f"Division : {self.num1 / self.num2}")


a = int(input("Enter first number : "))
b = int(input("Enter second number : "))
c = Calculator(a,b)
c.add()
c.subtract()
c.multiply()
c.divide()