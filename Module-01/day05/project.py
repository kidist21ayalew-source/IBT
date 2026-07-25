class Account:
    def __init__(self, owner, number, balance=0):
        self.owner=owner
        self.account_number=number
        self.__balance=balance

    def balance(self):
        return self.__balance
    def deposit(self,amount):
        if amount<=0:
            raise ValueError("Amount must be positive")
        self.__balance+=amount
    def withdraw(self, amount):
        if amount<=0:
            raise ValueError("Enter amount must be positive")
        if amount>self.__balance:
            raise ValueError("Insufficient funds for this withdrawal")
        self.__balance-=amount
    def statement(self):
        print(f"owner:{self.owner} | Account:{self.account_number}|Balance:{self.balance}") 

class SavindAccount(Account):
    def __init__(self, owner, number, balance=0,rate=0.5):
        super().__init__(owner, number,balance)
        self.rate =rate
    
    def add_interest(self):
        interest = self.balance * self.rate()
        self.deposit(interest)
        print(f"Added {interest} ETB interest.")
    def statement(self):
        print(f"Type: Saving | Owner: {self.owner} | Account: {self.account_number} | Balance: {self.balance} ETB | interest_rate: {self.rate}")
class CheckingAccount(Account):
    def __init__(self, owner, number, balance=0 ,overdraft_limit=20000):
        super().__init__(owner, number, balance) 
        self.overdraft_limit =overdraft_limit
    def statement(self):
     print (f"Type:Checking |Owner:{self.owner} |Account:{self.account_number} | Balance{self.balance}ETB |self.overdraft_limit{self.overdraft_limit}") 
    def withdraw(self, amount):
        if amount <=0:
            raise ValueError("Insufficent balance")
        if amount > (self.balance + self.overdraft_limit):
            raise ValueError("Exceeded overdraft limit")

        self._Account__balance -= amount

     
