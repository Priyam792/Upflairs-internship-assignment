# Write a program that:  
# ● Creates a file  
# ● Writes student data (name and marks)  
# ● Reads and displays the content

#Solution -->
students = [
    ("Namit", 92),
    ("Priyam", 85),
    ("Jatin", 78)
]
with open ("Student.txt" , "w") as f :
    for name , marks in students :
        f.write(f"{name} : {marks} \n")

with open("Student.txt", "r") as f:
    r = f.read()
    print(r)