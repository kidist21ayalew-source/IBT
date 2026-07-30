class Account:
    def __init__(self, number, balance=0.0):
        self.number = number
        self.balance = balance
        self.history = []  

    def deposit(self, amount):
        self.balance += amount
        self.history.append(("deposit", amount))

    def withdraw(self, amount):
        self.balance -=amount 
        self.history.append(("withdraw", amount))


class AccountRegistry:
    def __init__(self):
        self.accounts_dict = {}  
        self.insertion_order = []  
        self.global_stack = []  

    def add(self, acc):
        self.accounts_dict[acc.number] = acc
        self.insertion_order.append(acc)

    def find(self, number):
        return self.accounts_dict.get(number)

    def list_all(self):
        return self.insertion_order

    def transact_deposit(self, number, amount):
        acc = self.find(number)
        if acc:
            acc.deposit(amount)
            self.global_stack.append((acc, "deposit", amount))

    def transact_withdraw(self, number, amount):
        acc = self.find(number)
        if acc:
            acc.withdraw(amount)
            self.global_stack.append((acc, "withdraw", amount))

    def under_last(self):
        if not self.global_stack:
            return None
        acc, action, amount = self.global_stack.pop()
        if action == "deposit":
            acc.balance -= amount
            acc.history.pop()
        elif action == "withdraw":
            acc.balance += amount
            acc.history.pop()
        return (acc.number, action, amount)
