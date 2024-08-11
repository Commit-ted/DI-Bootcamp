class BankAccount:
    def __init__(self, owner, balance=0):
        # Initialize the owner and balance attributes
        self.owner = owner
        self.balance = balance
    
    def deposit(self, amount):
        # Add the amount to the balance if it's positive, otherwise print an error
        if amount > 0:
            self.balance += amount
            print(f"{amount} deposited. New balance: {self.balance}")
        else:
            print("Error: Deposit amount must be positive.")
    
    def withdraw(self, amount):
        # Subtract the amount from the balance if it's within the available funds, otherwise print an error
        if amount > self.balance:
            print("Error: Insufficient funds.")
        elif amount <= 0:
            print("Error: Withdrawal amount must be positive.")
        else:
            self.balance -= amount
            print(f"{amount} withdrawn. New balance: {self.balance}")
    
    def check_balance(self):
        # Print the current balance
        print(f"Current balance: {self.balance}")

# Usage Example
account = BankAccount("Alice")
account.deposit(100)
account.withdraw(30)
account.check_balance()
print( account)
