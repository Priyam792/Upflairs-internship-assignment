# Using Pandas built-in plotting, load or create a dataset with at least 4 numeric columns. Create:  
# • A histogram for marks distribution 
# • A box plot to visualize spread and outliers 
# • A pie chart showing category-wise percentage

# Solution -->

import pandas as pd
import matplotlib.pyplot as plt

data = {
    "Math": [88, 42, 78, 95, 64, 89, 25, 91, 82, 76],
    "Physics": [85, 55, 80, 92, 61, 87, 40, 89, 85, 73],
    "Chemistry": [90, 48, 75, 98, 68, 83, 35, 94, 80, 79],
    "Attendance": [92, 80, 85, 98, 75, 90, 60, 94, 88, 82],
    "Stream": ["Science", "Commerce", "Science", "Science", "Arts",
               "Science", "Commerce", "Science", "Arts", "Commerce"]
}

df = pd.DataFrame(data)

# Histogram
df["Math"].plot(kind="hist")
plt.title("Math Marks Distribution")
plt.show()

# Box Plot
df[["Math", "Physics", "Chemistry"]].plot(kind="box")
plt.title("Box Plot")
plt.show()

# Pie Chart
df["Stream"].value_counts().plot(kind="pie", autopct="%1.1f%%")
plt.title("Stream Distribution")
plt.show()