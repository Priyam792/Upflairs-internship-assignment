# 8. Create a dictionary: students = { "Aman": 78, "Riya": 92, "Kriti": 88, "Rahul": 95 } Write a program to: 
# ○ Find the student with the highest marks 
# ○ Find the student with the lowest marks 
# ○ Print only the students who scored more than 85 marks

#solutions -->

students = { "Aman": 78, "Riya": 92, "Kriti": 88, "Rahul": 95 }
print("Student with the highest marks =",max(students, key=lambda name: students[name]))
print("Student with the lowest marks =",min(students, key=lambda name: students[name]))
print("Students who scored more than 85 marks")
for name ,marks in students.items():
    if marks > 85:
        print(f"{name} : {marks}")