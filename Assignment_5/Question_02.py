# Create a 4×4 matrix using NumPy. Perform the following operations:  
# • Extract the diagonal elements 
# • Replace all even numbers with 0 
# • Find the index of the maximum value using argmax()

# Solution -->

import numpy as np

arr = np.arange(1,17).reshape(4,4)
print(f"Array : \n{arr}\n")

print(f"Diagonal elements : \n{np.diag(arr)}\n")

arr[arr%2==0]=0
print(f"Replacing even numbers with 0 : \n{arr}\n")

print(f"Index of maximum element : {np.unravel_index(arr.argmax(), arr.shape)}")