# Using Matplotlib, create the following plots from a student marks dataset (create the dataset yourself):  
# • A line plot showing marks trend across 5 subjects 
# • A bar chart comparing marks of 5 students 
# • Add proper title, xlabel, ylabel, legend, and grid to both plots

# Solution -->

import matplotlib.pyplot as plt

# Line plot: marks trend across 5 subjects
subjects = ["Math", "Science", "English", "CS", "Physics"]
marks = [85, 90, 78, 95, 88]

plt.figure()
plt.plot(subjects, marks, marker="o", label="Marks")
plt.title("Marks Trend Across Subjects")
plt.xlabel("Subjects")
plt.ylabel("Marks")
plt.legend()
plt.grid(True)
plt.show()

# Bar chart: comparison of 5 students
students = ["Aarav", "Priyam", "Rohan", "Diya", "Ananya"]
student_marks = [75, 90, 82, 88, 95]

plt.figure()
plt.bar(students, student_marks, label="Marks")
plt.title("Marks Comparison of Students")
plt.xlabel("Students")
plt.ylabel("Marks")
plt.legend()
plt.grid(True)
plt.show()