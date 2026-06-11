# 3.  Create a set: numbers = {10, 20, 30, 40, 50} Print: 
# ● Complete set  
# ● Length of the set  
# ● Check whether 30 is present in the set

#Solution -->

numbers = {10, 20, 30, 40, 50}
print(numbers)
print(f"Length of the set = {len(numbers)}")
if n := 30 in numbers:
    print("Yes 30 is present in the set.")
else:
    print("Not present")