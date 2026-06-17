# Write a user-defined function that accepts a list of integers and returns:  
# ● Count of even numbers  
# ● Sum of odd numbers  
# ● Use loops and conditional statements inside the function

def odsm(l):
    count = 0
    sum = 0
    for i in l :
        if i % 2 != 0:
            count += 1
        else :
            sum = sum + i
    print("The count of all odd numbers is",count)
    print("The sum of all even numbers is",sum)
lst = []
while True:
    a = input("Enter your number or Press 'Enter' to quit : ")
    if a == "":
        break
    lst.append(int(a))
odsm(lst)