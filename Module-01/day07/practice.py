#List index___o(1)(Only access number [2])

numbers = [10, 20, 30, 40, 50]

print(numbers[2])             


#Single Loop — O(n)(running time graw lineyarly with the number of element)

numbers = [10, 20, 30, 40, 50]

for num in numbers:
    print(num)

# Nested Loop — O(n²) (3*3=9 itration)   

numbers = [1, 2, 4]

for i in numbers:
    for j in numbers:
        print(i, j)

   
#Dictionary Lookup — O(1)( for age to find 34 )

student = {
    "name": "Kidist",
    "age": 34,
    "city": "Addis Ababa"
}

print(student["age"])

#Binary Search — O(log n) ( )

numbers = [2, 4, 6, 8, 10, 12, 14]

target = 10

left = 0
right = len(numbers) - 1

while left <= right:
    mid = (left + right) // 2

    if numbers[mid] == target:
        print("Found")
        break
    elif numbers[mid] < target:
        left = mid + 1
    else:
        right = mid - 1

# Qation No2 

import time
accounts_list = []

for i in range(100000):
    accounts_list.append(f"ACC{i}")

#Createadictionary
accounts_dict = {}

for i in range(100000):
    accounts_dict[f"ACC{i}"] = i

# Account to search
target = "ACC99999"

start = time.time()

found = target in accounts_list

end = time.time()

print("List lookup:", found)
print("Time:", end - start, "seconds")

start = time.time()

found = target in accounts_dict

end = time.time()

print("Dictionary lookup:", found)
print("Time:", end - start, "seconds")



#qation No 3
class Stack:

    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if len(self.items) == 0:
            return "Stack is empty"

        return self.items.pop()

    def peek(self):
        if len(self.items) == 0:
            return "Stack is empty"

        return self.items[-1]

# List of names
names = ["Kidist", "Dagem", "Hasset", "Abigiy"]

# Create a Stock
stack = Stack()

for name in names:
    stack.push(name)

reversed_names = []

while len(stack.items) > 0:
    reversed_names.append(stack.pop())

print("Original List:")
print(names)

print("Reversed List:")
print(reversed_names)





#qation No4


from collections import deque

# Create  queue
bank_queue = deque()

bank_queue.append("Kidist")
bank_queue.append("Dagem")
bank_queue.append("Hasset")
bank_queue.append("Abyigy")
bank_queue.append("Hana")

print("Customers in line:")
print(bank_queue)

print("\nServing customers:")

while bank_queue:
    customer = bank_queue.popleft()
    print(customer, "has been served.")

print("\nAll customers have been served.")



#qation No5
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    # Add a node 
    def push_front(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    
    def print_all(self):
        current = self.head

        while current is not None:
            print(current.data)
            current = current.next


# Create a linked list
linked_list = LinkedList()

linked_list.push_front("Kidist")
linked_list.push_front("Dagem")
linked_list.push_front("Hasset")
linked_list.push_front("Abyigy")

# Print the linked list
print("Linked List:")
linked_list.print_all()
