# 5. Create a dictionary: student = {"name":"Kriti", "age":20, "course":"Python"} Print: 
# ● Complete dictionary  
# ● Student name  
# ● Student age

#Solution -->

student = {"name":"Kriti", "age":20, "course":"Python"}
print(student)
print(student["name"])
print(student["age"])


# ● Student course Create a list: numbers = [12, 45, 7, 23, 56, 89, 34] Write a program to find: 
# o Largest element 
# o Second largest element 
# o Smallest element

numbers = [12, 45, 7, 23, 56, 89, 34]

numbers.sort()
print(f"Largest element : {numbers[-1]}")
print(f"Second largest element : {numbers[-2]}")
print(f"Smallest element : {numbers[0]}")