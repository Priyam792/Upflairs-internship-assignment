# Create at least two objects and display their grades.

#Solution -->

'''
    From question 5
'''

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
        print("---")

s1 = Student("Priyam", 82)
s1.show()
s2 = Student("Namit", 96) #<--------------------Second Object
s2.show()
