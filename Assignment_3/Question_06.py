# Create a class named BankAccount with: 
# o account_holder  
# o balance

# Create methods: 
# o deposit(amount)  
# o withdraw(amount)              
# Display the updated balance after each transaction

#Solution -->

class BankAccount :
    def __init__(self ,account_holder,balance):
        self.account_holder = account_holder
        self.balance = balance
    def deposite(self,amount):
        self.balance = self.balance + amount
        print(f"Updated balance : {self.balance}")
    def withdraw(self,amount):
        if amount > self.balance :
            print("Insufficient balance")
        else :
            self.balance = self.balance - amount
            print(f"Updated balance : {self.balance}")

b = BankAccount("Priyam",1000)
b.deposite(500)
b.withdraw(200)
b.withdraw(2500)