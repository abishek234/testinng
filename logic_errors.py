"""
logic_errors.py - Code with logical errors and edge cases
"""

def divide_numbers(a, b):
    # LOGIC ERROR: No zero division check
    return a / b

def find_maximum(numbers):
    # LOGIC ERROR: Empty list not handled
    max_val = numbers[0]  # Will crash if list is empty
    for num in numbers:
        if num > max_val:
            max_val = num
    return max_val

def calculate_average(scores):
    # LOGIC ERROR: Division by zero if empty list
    total = sum(scores)
    return total / len(scores)

def process_user_age(age):
    # LOGIC ERROR: No input validation
    if age > 18:
        return "Adult"
    else:
        return "Minor"
    # Doesn't handle negative ages or unrealistic ages like 200

def fibonacci(n):
    # LOGIC ERROR: Infinite recursion for negative numbers
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

def binary_search(arr, target):
    left = 0
    right = len(arr) - 1
    
    # LOGIC ERROR: Array not sorted check missing
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

class BankAccount:
    def __init__(self, initial_balance):
        self.balance = initial_balance
    
    def withdraw(self, amount):
        # LOGIC ERROR: No overdraft protection
        self.balance -= amount  # Can go negative
        return self.balance
    
    def transfer(self, other_account, amount):
        # LOGIC ERROR: No balance check before transfer
        self.balance -= amount
        other_account.balance += amount

def sort_students_by_grade(students):
    # LOGIC ERROR: Modifies original list without warning
    students.sort(key=lambda x: x.grade)
    return students

# LOGIC ERROR: Infinite loop
def count_to_infinity():
    counter = 0
    while True:
        counter += 1
        print(f"Count: {counter}")
        # No exit condition

def get_first_element(data):
    # LOGIC ERROR: No empty check
    return data[0]  # Will crash if data is empty
