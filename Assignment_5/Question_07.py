# Read a CSV file (you may create it manually) containing product sales data with columns: Product, Category, Sales, Region. 
# Perform:  
# • Group by Category and calculate total Sales using groupby() and agg() 
# • Find the top 3 products by sales using sort_values() and head() 

# Solution -->

import pandas as pd

df = pd.read_csv("/home/priyam/Projects/Training/Assignment_5/sales.csv")
print(f"CSV file content : \n{df}\n")
category = df.groupby("Category").agg(Total_Sales=("Sales", "sum")).reset_index()
print(f"Group by Category : \n{category}\n")

a = df.sort_values(by="Sales",ascending=False).head(3)
print(f"Top 3 products by sales : \n{a}")