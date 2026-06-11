# 1.  Create a tuple: my_tuple = (10, 20, 30, 40, 50) Print: 
# ● First element  
# ● Last element  
# ● Length of the tuple  
# ● Elements from index 1 to 3

#solution ---->

my_tuple = (10, 20, 30, 40, 50)
print(my_tuple[0])
print(my_tuple[-1])
print(len(my_tuple))
for i in range(1,4):
    print(f"Element at index {i} = {my_tuple[i]}")
