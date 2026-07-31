#Quation No1

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def insert(root, value):
    if root is None:
        return Node(value)

    if value < root.value:
        root.left = insert(root.left, value)
    else:
        root.right = insert(root.right, value)

    return root


def inorder(root):
    if root is not None:
        inorder(root.left)
        print(root.value)
        inorder(root.right)


balances = [5000, 2000, 7000, 1000, 3000, 6000, 8000]

root = None

for balance in balances:
    root = insert(root, balance)

print("Balances in sorted order:")
inorder(root)


#Qation No 2 

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def height(node):
    if node is None:
        return 0

    left_height = height(node.left)
    right_height = height(node.right)

    return max(left_height, right_height) + 1


# Build the tree
root = Node(50)

root.left = Node(30)
root.right = Node(70)

root.left.left = Node(20)
root.left.right = Node(40)

root.right.left = Node(60)
root.right.right = Node(80)

print("Tree height:", height(root))



#Qation No 3

from collections import deque

def bfs(graph, start):
    visited = set()
    queue = deque([start])

    while queue:
        vertex = queue.popleft()

        if vertex not in visited:
            visited.add(vertex)

            for neighbor in graph[vertex]:
                if neighbor not in visited:
                    queue.append(neighbor)

    return visited


graph = {
    "A": ["B", "C"],
    "B": ["A", "D", "E"],
    "C": ["A", "F"],
    "D": ["B"],
    "E": ["B", "F"],
    "F": ["C", "E"]
}

reachable = bfs(graph, "A")

print("Reachable vertices:", reachable)


#Qation No4

def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()

    visited.add(start)
    print(start)

    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

    return visited


graph = {
    "A": ["B", "C"],
    "B": ["A", "D", "E"],
    "C": ["A", "F"],
    "D": ["B"],
    "E": ["B", "F"],
    "F": ["C", "E"]
}

reachable = dfs(graph, "A")

print("Reachable vertices:", reachable)




#Qation No5

import heapq
priority_queue =[]

# Push five tasks in mixed order
heapq.heappush(priority_queue, (2, "Do homework"))
heapq.heappush(priority_queue, (3, "Do project"))
heapq.heappush(priority_queue, (5, "Watch TV"))
heapq.heappush(priority_queue, (1, "Study Python"))
heapq.heappush(priority_queue, (4, "Exercise"))

print("Tasks by priority:")

while priority_queue:
    priority, task = heapq.heappop(priority_queue)
    print(priority, "-", task)