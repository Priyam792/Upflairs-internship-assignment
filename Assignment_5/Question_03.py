# Write a program to create two 3×3 NumPy arrays and perform element-wise addition, subtraction, and matrix multiplication. 
# Display results with proper labels. 

# Solution -->

import numpy as np 

a = np.arange(1,10).reshape(3,3)
b = np.arange(10,19).reshape(3,3)
print(f"Matrix 1 : \n{a}\n")
print(f"Matrix 2 : \n{b}\n")
print(f"Addition : \n{a+b}\n")
print(f"Subtraction : \n{a-b}\n")
print(f"Multiplication : \n{a@b}\n")