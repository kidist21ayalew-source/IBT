#account.py
class Account:
    def __init__(self, owner, number, balance=0):
        self.owner = owner
        self.account_number = number
        self.__balance = balance
    @property
    def balance(self):
        return self.__balance
    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Amount  shoud  be positive")
        self.__balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Enterd Amount must be positive")
        if amount > self.__balance:
            raise ValueError("Insufficient amount")
        self.__balance -= amount

    def statement(self):
        print(f"Owner: {self.owner} | Account: {self.account_number} | Balance: {self.__balance} ETB")


# creat object for the bove class

Account_1=Account("kidist", "10001264", 1500)
Account_2 =Account("Hasset", "10001315", 1000)
Account_3 =Account("Dagem", "10001216", 2000)

print("Initial statements ")

Account_1.statement()
Account_2.statement()
Account_3.statement()


print(f"acc_1 balance via property: {Account_1.balance}")

try:
    Account_1.balance = 999999

except AttributeError as e:
     
    print(f"Blocked direct edit: {e}")

Account_1.deposit(800)

print(" After depositing 200 to acc_1")

Account_1.statement()
Account_1.withdraw(150)

print("After withdrawing 200 from Account_1")

Account_1.statement()
try:

    Account_1.deposit(-50)  

except ValueError as e:
    print(f"Deposit rejected: {e}")

    
try:
        Account_1.withdraw(999999)
except ValueError as e:
        print(f"Withdrawal rejected: {e}")

print("acc_2 remains unaffected ---")
Account_2.statement()

  
