# Create a DataFrame with some missing values intentionally placed in the Marks and City columns. Then:  
# • Identify missing values using isnull() 
# • Fill missing marks with the column mean using fillna() 
# • Drop rows where City is missing using dropna()

# Solution -->

import pandas as pd
import numpy as np

data = {
    "Name": ["Priyam", "Aarav", "Ananya", "Rohan", "Diya", "Kabir", "Meera", "Vikram", "Isha", "Aditya"],
    "Age": [19, 21, 20, 22, 19, 23, 20, 21, 22, 20],
    "Marks": [87.0, np.nan, 78.0, 85.0, np.nan, 64.0, 89.0, np.nan, 91.0, 82.0],
    "City": ["Pilani", "Mumbai", None, "Bangalore", "Jaipur", "Pune", None, "Kota", "Chennai", "Kolkata"]
}

df = pd.DataFrame(data)
print(f"Total missing values in each column : \n{df.isnull().sum()}\n{df.isnull()}\n")

a = df["Marks"].mean()
df["Marks"] = df["Marks"].fillna(a)
print(f"Filled missign marks with the column mean : \n{df}\n")

df = df.dropna(subset=["City"])
print(f"Droped rows where city is missing : \n{df}")