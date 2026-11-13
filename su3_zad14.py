class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance = self.balance + amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance = self.balance - amount
        else:
            print("Недостатъчна наличност!")

    def print(self):
        print("Собственик:", self.owner)
        print("Баланс:", self.balance, "лв.")


class SavingsAccount(Account):
    def __init__(self, owner, balance, interest_rate):
        super().__init__(owner, balance)
        self.interest_rate = interest_rate

    def add_interest(self):
        interest = self.balance * self.interest_rate / 100
        self.balance = self.balance + interest
        print("Начислена лихва:", interest, "лв.")

    def print(self):
        super().print()
        print("Годишна лихва:", self.interest_rate, "%")


s1 = SavingsAccount("Иван Иванов", 1000, 5)

s1.print()
print()

s1.add_interest()
print()

s1.print()