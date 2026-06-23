# Create a 1D NumPy array of 20 random integers between 1 and 100.
# Find the minimum, maximum, mean, and standard deviation without using Python built-in functions — use only NumPy aggregation functions

# Solution -->

import numpy as np 

arr =  np.random.randint(1,101,20)
print(f"Random array : {arr}")
print("Minimum :", arr.min())
print("Maximum :", arr.max())
print("Mean    :", arr.mean())
print("Std Dev :", arr.std())