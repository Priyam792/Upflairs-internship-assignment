# 1. Write a program that takes a list of numbers and prints all prime numbers in the list using loops. 
# Do not use any built-in prime-checking functions.

#Solution -->


def is_prime(l):
    lst1 =[]   
    for n in l:
        
        if n < 2:
            continue

        for i in range(2, n):
            if n % i == 0:   
                break   
        else :
            lst1.append(n)
    print(lst1)    
lst = []
while True:
    a = input("Enter numbers in list or Press 'Enter' to quit : ")
    if a == "":
        break
    lst.append(int(a))
is_prime(lst)

    