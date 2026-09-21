class BankAccount:
    def calculate_interest(self, balance):
        print("Interest calculation")


class SavingsAccount(BankAccount):
    def calculate_interest(self, balance):
        interest = balance * 4 / 100
        print("Savings Account Interest =", interest)


class CurrentAccount(BankAccount):
    def calculate_interest(self, balance):
        interest = balance * 2 / 100
        print("Current Account Interest =", interest)


class FixedDepositAccount(BankAccount):
    def calculate_interest(self, balance):
        interest = balance * 7 / 100
        print("Fixed Deposit Interest =", interest)


# Create objects
accounts = [
    SavingsAccount(),
    CurrentAccount(),
    FixedDepositAccount()
]

balance = 100000

# Runtime Polymorphism
for account in accounts:
    account.calculate_interest(balance)