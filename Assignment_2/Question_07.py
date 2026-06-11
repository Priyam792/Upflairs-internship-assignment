# 7. Create a tuple: data = (5, 10, 15, 20, 25, 30, 35) Write a program to: 
# ○ Count how many elements are divisible by 5 
# ○ Find the sum of all elements 
# ○ Find the average of the tuple

#Solutions -->

data = (5, 10, 15, 20, 25, 30, 35)
c = 0
for i in data :
    if i % 5 == 0:
        c += 1
print(f"Count = {c}")
print(f"Sum = {sum(data)}")
print(f"Average = {sum(data)/len(data)}")