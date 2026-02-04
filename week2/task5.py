class BankAccount:
    def __init__(self, initial_balance=0):
        self.__balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Поповнено: {amount}")
        else:
            print("Сума повинна бути додатною")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Знято: {amount}")
        else:
            print("Недостатньо коштів або некоректна сума")

    def get_balance(self):
        return self.__balance

account = BankAccount(1000)

print(f"Поточний баланс: {account.get_balance()}")