# 6. Create a list: arr = [10, 20, 30, 40, 50, 60] 
# Write a function that takes the list as input and returns the list in reverse order without using the reverse() method.

def rev(l):
    l1 =[]
    for i in range(len(l)-1,-1,-1):
        l1.append(l[i])

    print(l1)
        

arr = [10, 20, 30, 40, 50, 60]
rev(arr)