# 10. Write a function: 
# find_duplicates(arr) that takes a list as input and prints all duplicate elements present in the list.            
# Example: arr = [10, 20, 30, 20, 40, 10, 50, 30]             
# Output:            Duplicate elements are: 10 20 30

#Solution -->

def find_duplicates(arr):
    a =[]
    d =[]
    for i in arr:
        if i in a:
            d.append(i)
        else:
            a.append(i)
    print(f"Duplicated items are : {d}")

arr = [10, 20, 30, 20, 40, 10, 50, 30]       
find_duplicates(arr)