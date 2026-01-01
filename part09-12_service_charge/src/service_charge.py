# WRITE YOUR SOLUTION HERE:

class BankAccount: 
    def __init__(self, owner: str, account: int, balance: float):
        self.__owner = owner
        self.__account = account
        self.__balance = balance

    @property
    def balance(self):
        return self.__balance

    def deposit(self, amount: float):
        if amount > 0:
            self.__balance += amount
            self.__service_charge()
        else:
            raise ValueError("Amount must be positive.")

    def withdraw(self, amount: float):
        if amount <= self.__balance:
            self.__balance -= amount
            self.__service_charge()
        else: 
            raise ValueError("Insufficient funds for withdrawal.")

    def __service_charge(self):
        if self.__balance > 0:
            self.__balance *= 0.99
        else:
            raise ValueError("Insufficient funds for service charge.")


# account = BankAccount("Randy Riches", "12345-6789", 1000)
# account.withdraw(100)
# print(account.balance)
# account.deposit(100)
# print(account.balance)