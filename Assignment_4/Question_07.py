# Create a BankAccount class with private attributes for balance. 
# Provide methods to deposit and withdraw money. Ensure balance cannot be accessed directly.

#Solution -->

class BankAccount :
    def __init__(self,balance):
        self.__balance = balance
    
    def deposit(self,amount):
        if amount > 0:
            self.__balance = self.__balance + amount
            print(f"Deposited : {amount}")
        else :
            print("Invalid amount")

    def withdraw(self,amount):
        if amount <= self.__balance:
            self.__balance = self.__balance - amount
            print(f"Amount withdrawed : {amount}")
        else :
            print("Isufficient balance!")

    def fbalance(self):
        print(f"Balance : {self.__balance}")

b = BankAccount(1000)
b.deposit(500)
b.withdraw(200)
b.fbalance()