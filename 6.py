class BankAccount:
    def __init__(self, account_no, balance):
        self.account_no = account_no
        self.balance = balance


class SavingsAccount(BankAccount):
    def __init__(self, account_no, balance, rate):
        super().__init__(account_no, balance)
        self.rate = rate

    def interest(self):
        return self.balance * self.rate / 100


class PremiumSavingsAccount(SavingsAccount):
    def __init__(self, account_no, balance, rate, benefits):
        super().__init__(account_no, balance, rate)
        self.benefits = benefits

    def display(self):
        print("Account No =", self.account_no)
        print("Balance =", self.balance)
        print("Interest Rate =", self.rate, "%")
        print("Interest =", self.interest())
        print("Benefits =", self.benefits)


p = PremiumSavingsAccount(101, 50000, 6, "Free Insurance")

p.display()