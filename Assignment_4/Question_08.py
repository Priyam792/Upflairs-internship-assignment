# Write a program that takes two numbers from the user and performs division.  
# ● Handle the following exceptions:  
# ● Division by zero
# ● Invalid input type

#Solution -->
try :
    a = int(input("Enter a number : "))
    b = int(input("Enter second number : "))
    print(f"{a}/{b} = {a/b}")
except ValueError:
    print("Invalid number!!")
except ZeroDivisionError:
    print("Cannot divisible by Zero")