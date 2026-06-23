# Merge two DataFrames:  
# • DataFrame 1: StudentID, Name, Department 
# • DataFrame 2: StudentID, Marks, Grade 
# • Merge on StudentID and display students who scored Grade 'A' 

# Solution -->

import pandas as pd


data1 = {
    "StudentID": [101, 102, 103, 104, 105],
    "Name": ["Priyam", "Aarav", "Ananya", "Rohan", "Diya"],
    "Department": ["Computer Science", "Electronic Engineering", "Mechanical", "Computer Science", "Information Technology"]
}

data2 = {
    "StudentID": [101, 102, 103, 104, 105],
    "Marks": [87, 92, 78, 85, 95],
    "Grade": ["B+", "A", "C", "B", "A"]
}

df1 = pd.DataFrame(data1)
df2 = pd.DataFrame(data2)

merged = pd.merge(df1, df2, on="StudentID")
merged = merged[merged["Grade"] == "A"]
print(f"Students with grade 'A'.")
print(merged)