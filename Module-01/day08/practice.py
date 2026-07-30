def total(nums):

    if len(nums) == 0:
        return 0

    return nums[0] + total(nums[1:])


numbers = [5, 2, 8]

print(total(numbers)) 


#qation No2

def count_down(n):
  if n==0:
      return
  print(n)
    
  count_down( n-1) 
  
count_down(5)



#qation No3


import random


def merge(left, right):
    result = []

    i = 0
    j = 0

    while i < len(left) and j < len(right):

        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result


def merge_sort(items):

    if len(items) <= 1:
        return items

    middle = len(items) // 2

    left = merge_sort(items[:middle])
    right = merge_sort(items[middle:])

    return merge(left, right)


for _ in range(10):

    numbers = random.sample(range(100), 10)

    my_sort = merge_sort(numbers)
    python_sort = sorted(numbers)

    print("Original :", numbers)
    print("Merge Sort:", my_sort)
    print("sorted()  :", python_sort)
    print("Match:", my_sort == python_sort)
    print("-" * 40)
  


#qation No4


accounts = [
    ("Kidist", 2500),
    ("Dagem", 1800),
    ("Hasset", 2200),
    ("Abigyal", 1500),
    ("Habtamu", 2750)
]

# Sort by balance in descending  order
sorted_accounts = sorted(accounts, key=lambda account: account[1], reverse=True)

print("Accounts sorted by balance ( highest to lowest):")
for name, balance in sorted_accounts:
    print(f"{name}: ${balance}")



#qation No5

def has_pair(nums, target):
    left = 0
    right = len(nums) - 1

    while left < right:
        current_sum = nums[left] + nums[right]

        if  current_sum == target:
            return True
        elif current_sum < target:
            left += 1
        else:
           right -= 1

    return False


# Test
numbers = [1, 2, 3, 4, 6, 8, 10]

print(has_pair(numbers, 10))  
print(has_pair(numbers, 7))   
print(has_pair(numbers, 20))  