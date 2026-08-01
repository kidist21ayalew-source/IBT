

from collections import deque

class Account:  # account class
    def __init__(self, number, owner, balance):
        self.number = number
        self.owner = owner
        self.balance = balance

    def __str__(self):
        return f"{self.number} - {self.owner} - Balance: ${self.balance}"



class Branch:                  #branch class
    def __init__(self, name):
        self.name = name
        self.children = []      # Sub-branches
        self.accounts = []      # Accounts in this branch

    def add_child(self, branch):
        self.children.append(branch)

    def add_account(self, account):
        self.accounts.append(account)

    def total_balance(self):
        total = sum(account.balance for account in self.accounts)

    
        for child in self.children:
            total += child.total_balance()

        return total
def bfs(transfers, start):
    visited = set()
    queue = deque([start])

    while queue:
        current = queue.popleft()

        if current not in visited:
            visited.add(current)

            for neighbor in transfers.get(current, []):
                if neighbor not in visited:
                    queue.append(neighbor)

    return visited



#  Test Create Accounts

a1 = Account(101264, "kidist", 500)
a2 = Account(101213, "Dagem", 800)
a3 = Account(101315, "Hasset", 1200)
a4 = Account(101243, "Abigeyal", 900)
a5 = Account(101219, "Habtamu", 600)


# Create Branches

head = Branch("Head Office")

north = Branch("North Region")
south = Branch("South Region")

addis = Branch("Addis Branch")
bahir = Branch("Bahir Dar Branch")
hawassa = Branch("Hawassa Branch")

head.add_child(north)
head.add_child(south)

north.add_child(addis)
north.add_child(bahir)

south.add_child(hawassa)


addis.add_account(a1)
addis.add_account(a2)

bahir.add_account(a3)

hawassa.add_account(a4)
hawassa.add_account(a5)



# Calculate Total Balance

print("Head Office Total Balance:")
print(head.total_balance())



# Transfers Graph

transfers = {
    101264: [101213, 101315],
    101213: [101243],
    101315: [101219],
    101243: [],
    101219: []
}



print("\nAccounts reachable from 101264:")
print(bfs(transfers, 101264))