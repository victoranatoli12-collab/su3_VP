
class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print("Успешно внесена сума:", amount)
        else:
            print("Невалидна сума")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            print("Успешно изтеглена сума:", amount)
        else:
            print("Недостатъчна наличност")

    def print(self):
        print("Собственик:", self.owner)
        print("Баланс:", self.balance, "лв.")


a1 = Account("Иван", 1000)

a1.print()
a1.deposit(500)
a1.withdraw(200)
a1.print()
