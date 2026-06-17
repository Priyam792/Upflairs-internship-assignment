# Create a Student class with attributes: name, marks. Add a method to calculate grade based on marks.

#Solution -->

class Student :
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
    
    def grade(self):
        if self.marks >= 90:
            return "A"
        elif self.marks >= 80:
            return "B"
        elif self.marks >= 70:
            return "C"
        elif self.marks >= 55:
            return "D"
        elif self.marks >= 35:
            return "E"
        else:
            return "F"
        
    def show(self):
        print(f"Name = {self.name}")
        print(f"Marks = {self.marks}")
        print(f"Grade = {self.grade()}")

s1 = Student("Priyam", 92)
s1.show()
