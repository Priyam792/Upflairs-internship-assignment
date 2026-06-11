# 9. Write a function: count_frequency(arr) that takes a list as input and prints the frequency of each element. 
# Example: arr = [1, 2, 2, 3, 1, 4, 2]  Output:   
# 1 -> 2 times 
# 2 -> 3 times 
# 3 -> 1 time 
# 4 -> 1 time

#Solution -->

def count_frequency(arr):
    freq = {}
    for num in arr:
        if num in freq:
            freq[num] += 1
        else :
            freq[num] = 1
    for nums , frq in freq.items():
        print(f"{nums} -> {frq} {'time' if frq <=1 else 'times'}")

arr = [1, 2, 2, 3, 1, 4, 2]
count_frequency(arr)
    
