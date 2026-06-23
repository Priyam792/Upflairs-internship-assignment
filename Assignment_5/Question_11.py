# Using Seaborn, create a dataset of at least 50 records with columns Age, Salary, Department, Experience. Plot:  
# • A scatter plot of Age vs Salary with hue as Department 
# • A heatmap showing correlation between numeric columns 
# • A bar plot showing average Salary per Department

# Solution -->

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.DataFrame({
    "Age": np.random.randint(22, 50, 50),
    "Salary": np.random.randint(25000, 100000, 50),
    "Experience": np.random.randint(1, 20, 50),
    "Department": np.random.choice(["HR", "IT", "Sales"], 50)
})

# Scatter Plot
sns.scatterplot(data=df, x="Age", y="Salary", hue="Department")
plt.title("Age vs Salary")
plt.show()

# Heatmap
sns.heatmap(df.corr(numeric_only=True), annot=True)
plt.title("Correlation Heatmap")
plt.show()

# Bar Plot
sns.barplot(data=df, x="Department", y="Salary")
plt.title("Average Salary per Department")
plt.show()