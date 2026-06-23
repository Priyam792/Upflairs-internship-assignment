# Create a DataFrame of at least 10 students with columns: Name, Age, Marks, City. Perform the following:  
# • Display the first 5 rows using head() 
# • Show basic statistics using describe() 
# • Filter students who scored more than 75 marks 
# • Sort by Marks in descending order

# Solution -->

import pandas as pd
data = {
    "Name": [
        "Priyam", "Aarav", "Ananya", "Rohan", "Diya", "Kabir", "Meera", "Vikram", "Isha", "Aditya"
        ],
    "Age": [19, 21, 20, 22, 19, 23, 20, 21, 22, 20],
    "Marks": [87, 92, 78, 85, 95, 64, 89, 73, 91, 82],
    "City": [
        "Pilani", "Mumbai", "Delhi", "Bangalore", "Jaipur", 
        "Pune", "Hyderabad", "Kota", "Chennai", "Kolkata"
    ]
}

df = pd.DataFrame(data)
print(f"First 5 rows : \n{df.head()}\n")
print(f"Basic statistics : \n{df.describe()}\n")
a = df[df["Marks"]>75]
print(f"Students who have more then 75 marks : \n{a}\n")
b = df.sort_values(by="Marks",ascending=False)
print(f"Marks in descending order : \n{b}")