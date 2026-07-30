class Account:
    def __init__(self, owner, number, balance=0):
        self.owner = owner
        self.number = number
        self.balance = balance
        self.transactions = []

    def deposit(self, amount):
        self.balance += amount
        self.transactions.append(amount)

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            self.transactions.append(-amount)
        else:
            print("Insufficient amount")


class AccountRegistry:
    def __init__(self):
        self.accounts = []

    def add_account(self, account):
        self.accounts.append(account)


    # 1. Balance Leaderboard
  

    def top_by_balance(self, n):
        return sorted(
            self.accounts,
            key=lambda a: a.balance,
            reverse=True
        )[:n]

  
    # 2. Binary Search
    
    def binary_search(self, accounts, number, left, right):

        if left > right:
            return None

        mid = (left + right) // 2

        if accounts[mid].number == number:
            return accounts[mid]

        elif number < accounts[mid].number:
            return self.binary_search(accounts, number, left, mid - 1)

        else:
            return self.binary_search(accounts, number, mid + 1, right)

    def find_by_number(self, number):

        sorted_accounts = sorted(
            self.accounts,
            key=lambda a: a.number
        )

        return self.binary_search(
            sorted_accounts,
            number,
            0,
            len(sorted_accounts) - 1
        )


    # 3. Recursive Transaction Total
   

    def recursive_total(self, transactions):

        if len(transactions) == 0:
            return 0

        return transactions[0] + self.recursive_total(transactions[1:])

    def total_transactions(self, number):

        account = self.find_by_number(number)

        if account is None:
            return None

        return self.recursive_total(account.transactions)



# Test Program


registry = AccountRegistry()

a1 = Account("Kidist", 1001264, 2000)
a1.deposit(500)
a1.withdraw(100)

a2 = Account("Dagem", 1001213, 1500)
a2.deposit(200)

a3 = Account("Hasset", 1001315, 2000)
a3.deposit(1000)
a3.withdraw(300)

registry.add_account(a1)
registry.add_account(a2)
registry.add_account(a3)


print("Top 2 Accounts by Balance")
for account in registry.top_by_balance(2):
    print(account.owner, account.balance)

print()

# Binary Search
account = registry.find_by_number(1001315)
if account:
    print("Found Account:")
    print(account.owner, account.balance)

print()


print("Transaction Total for Kidist:")
print(registry.total_transactions(1001264))