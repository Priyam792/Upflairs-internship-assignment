# Using np.linspace() and np.zeros() and np.ones(), create three different arrays and stack them vertically using np.vstack(). 
# Display the final stacked array

# Solution -->

import numpy as np

a = np.linspace(0,10,6)
b = np.zeros(6)
c = np.ones(6)
print(np.vstack((a,b,c)))