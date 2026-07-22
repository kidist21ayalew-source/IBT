stock = {}
try:
    with open("stock.txt", "r") as f:
        for line in f:
            line = line.strip()
            item, qty = line.split(",")
            stock[item] = int(qty)

except FileNotFoundError:
    print("stock.txt not found.")

# Function to update stock
def update_stock(item, amount):
    if item in stock:
        stock[item] += amount
    else:
        print("Item not found.")

# Example updates
update_stock("paracetamon", -5)

# Print low stock
print("Low stock items:")
for item, qty in stock.items():
    if qty < 10:
        print(item, qty)

