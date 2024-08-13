class BankAccount:
    total_accounts = 0
    all_accounts = []
    interest_rate = 0.02  # Default interest rate for savings accounts

    def __init__(self, account_number, account_type, initial_balance=0.0):
        self.account_number = account_number
        self._balance = initial_balance
        self.account_type = account_type
        self.transaction_history = []
        BankAccount.total_accounts += 1
        BankAccount.all_accounts.append(self)

    @classmethod
    def get_total_accounts(cls):
        return cls.total_accounts

    @classmethod
    def find_account_by_number(cls, account_number):
        for account in cls.all_accounts:
            if account.account_number == account_number:
                return account
        return None

    @classmethod
    def total_balances(cls):
        return sum(account._balance for account in cls.all_accounts)

    @property
    def balance(self):
        return self._balance

    @property
    def account_type(self):
        return self._account_type

    @account_type.setter
    def account_type(self, value):
        if value.lower() in ["savings", "checking"]:
            self._account_type = value.lower()
        else:
            raise ValueError("Invalid account type. Must be 'savings' or 'checking'.")

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            self.transaction_history.append(f"Deposited: ${amount}")
        else:
            raise ValueError("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > 0:
            if self._balance >= amount:
                self._balance -= amount
                self.transaction_history.append(f"Withdrew: ${amount}")
            else:
                raise ValueError("Insufficient funds.")
        else:
            raise ValueError("Withdrawal amount must be positive.")

    def apply_interest(self):
        if self.account_type == "savings":
            interest = self._balance * BankAccount.interest_rate
            self._balance += interest
            self.transaction_history.append(f"Interest applied: ${interest:.2f}")
        else:
            raise ValueError("Interest can only be applied to savings accounts.")


# Creating multiple bank accounts
account1 = BankAccount(account_number=1, account_type="savings", initial_balance=1000)
account2 = BankAccount(account_number=2, account_type="checking", initial_balance=500)
account3 = BankAccount(account_number=3, account_type="savings", initial_balance=1500)

# Deposit and Withdraw operations
account1.deposit(500)
account1.withdraw(200)
account2.deposit(100)
account2.withdraw(50)
account3.deposit(300)
account3.withdraw(1000)

# Apply interest to savings accounts
account1.apply_interest()
account3.apply_interest()

# Display account details
print(f"Account 1 balance: ${account1.balance}")
print(f"Account 2 balance: ${account2.balance}")
print(f"Account 3 balance: ${account3.balance}")

# Display transaction history
print(f"Account 1 transaction history: {account1.transaction_history}")
print(f"Account 2 transaction history: {account2.transaction_history}")
print(f"Account 3 transaction history: {account3.transaction_history}")

# Find an account by account number
found_account = BankAccount.find_account_by_number(2)
if found_account:
    print(f"Found Account 2, Balance: ${found_account.balance}")

# Total number of accounts and total balances
print(f"Total accounts created: {BankAccount.get_total_accounts()}")
print(f"Total balance across all accounts: ${BankAccount.total_balances()}")
