class BankAccount:
    accounts = []
    def __init__(self, int_rate = 0.02, balance = 500.00):
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.accounts.append(self)

    def deposit(self, amount):
        self.balance += amount
        return self
    
    def withdraw(self, amount):
        if amount <= self.balance and amount >= 0:
            self.balance -= amount
        elif amount >= self.balance:
            print("Insufficient funds: Charing a $5 fee")
            self.balance -= 5.00
        return self

    def display_account_info(self):
        print(f"Account Balance: {self.balance}")
        return self

    def yield_interest(self):
        if self.balance >= 0:
            self.balance += (self.balance * 2) * self.int_rate
        return self

    @classmethod
    def print_all_accounts(cls):
        for account in cls.accounts:
            account.display_account_info()

Torrei = BankAccount(0.02, 10000)
Arnold = BankAccount(1000)

Torrei.deposit(20).deposit(50).deposit(1000).withdraw(800).yield_interest()
Arnold.deposit(50).deposit(0.02).withdraw(20.41).withdraw(19.99).withdraw(0.01).withdraw(4.58).yield_interest

BankAccount.print_all_accounts()