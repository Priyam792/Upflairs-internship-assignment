# Create a subplot layout of 2 rows × 2 columns using Matplotlib containing:  
# • Line plot 
# • Scatter plot 
# • Bar chart 
# • Histogram All using the same dataset. Add a main title using suptitle()

# Solution -->

import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [10, 25, 15, 30, 20]

fig, ax = plt.subplots(2, 2, figsize=(8, 6))

# Line Plot
ax[0, 0].plot(x, y)
ax[0, 0].set_title("Line Plot")

# Scatter Plot
ax[0, 1].scatter(x, y)
ax[0, 1].set_title("Scatter Plot")

# Bar Chart
ax[1, 0].bar(x, y)
ax[1, 0].set_title("Bar Chart")

# Histogram
ax[1, 1].hist(y)
ax[1, 1].set_title("Histogram")

plt.suptitle("Matplotlib Subplots")
plt.tight_layout()
plt.show()