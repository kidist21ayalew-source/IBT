#day 06 project.py
# -------------------------
# Singleton
# -------------------------

class BankConfig:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)

            # Shared settings
            cls._instance.interest_rate = 0.05
            cls._instance.overdraft_limit = 2000

        return cls._instance


# -------------------------
# Observer Classes
# -------------------------

class SMSAlert:
    def update(self, message):
        print(f"SMS Alert: {message}")


class AuditLog:
    def update(self, message):
        print(f"Audit Log: {message}")


# -------------------------
# Base Account
# -------------------------

class Account:
    def __init__(self, owner, number, balance=0):
        self.owner = owner
        self.account_number = number
        self._balance = balance
        self.observers = []

    def subscribe(self, observer):
        self.observers.append(observer)

    def _notify(self, message):
        for observer in self.observers:
            observer.update(message)

    def balance(self):
        return self._balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Amount must be positive.")

        self._balance += amount
        self._notify(f"{self.owner} deposited {amount} ETB")

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Amount must be positive.")

        if amount > self._balance:
            raise ValueError("Insufficient amount.")

        self._balance -= amount
        self._notify(f"{self.owner} withdrew {amount} ETB")

    def statement(self):
        print(
            f"Owner: {self.owner} | "
            f"Account: {self.account_number} | "
            f"Balance: {self.balance()} ETB"
        )

# Savings Account

class SavingAccount(Account):

    def add_interest(self):
        config = BankConfig()
        interest = self.balance() * config.interest_rate
        self.deposit(interest)

    def statement(self):
        print(
            f"Type: Savings | " "Owner: {self.owner} | " "Account: {self.account_number} | "  f"Balance: {self.balance()} ETB"
        )

# Current Account

class CurrentAccount(Account):

    def withdraw(self, amount):
        config = BankConfig()

        if amount <= 0:
            raise ValueError("Amount must be positive.")

        if amount > self.balance() + config.overdraft_limit:
            raise ValueError("Exceeded overdraft limit.")

        self._balance -= amount
        self._notify(f"{self.owner} withdrew {amount} ETB")

    def statement(self):
        print(
            f"Type: CurrentAccount |"
            f"Owner: {self.owner} | " 
            f"Account: {self.account_number} | "
            f"Balance: {self.balance()} ETB"
        )


class AccountFactory:

    @staticmethod
    def create(kind, owner, number, balance=0):

        if kind.lower() == "savings":
            return SavingAccount(owner, number, balance)

        elif kind.lower() == "current":
            return CurrentAccount(owner, number, balance)

        else:
            raise ValueError("Invalid account type.")



# Testing

config1 = BankConfig()
config2 = BankConfig()

print("Same config object:", config1 is config2)

# Observers
sms = SMSAlert()
audit = AuditLog()

# Factory
acc1 = AccountFactory.create("savings", "Kidist", "1001", 5000)
acc2 = AccountFactory.create("current", "Abel", "1002", 3000)

# Subscribe observers
acc1.subscribe(sms)
acc1.subscribe(audit)

acc2.subscribe(sms)
acc2.subscribe(audit)

# Transactions
acc1.deposit(1000)
acc1.add_interest()

acc2.withdraw(1500)

# Statements
acc1.statement()
acc2.statement()