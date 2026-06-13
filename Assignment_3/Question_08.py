# Create a class named Person with attributes: 
# o name  
# o age            
# Create a child class Student with an additional attribute: 
# o roll_number            
# Display all the details using an object of the Student class

#Solution -->

class Person :
    def __init__(self,name , age):
        self.name = name
        self.age = age

class Student(Person):
    def __init__(self,name,age,roll_number):
        super().__init__(name,age)
        self.roll_number = roll_number
    def show(self):
        print(F"Name = {self.name}")
        print(F"Age = {self.age}")
        print(F"Roll number = {self.roll_number}")


s = Student("Priyam",19,"24EBKAI946")
s.show()
