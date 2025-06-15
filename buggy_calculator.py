"""
buggy_calculator.py - A calculator with intentional bugs for testing
This file contains various types of issues that the AI agents should detect
"""

import math
import time

class Calculator:
    def __init__(self)  # SYNTAX ERROR: Missing colon
        self.history = []
        self.debug_mode = True
    
    def add(self, a, b):
        result = a + b
        self.history.append(f"Added {a} + {b} = {result}")
        return result
    
    def divide(self, a, b):
        # LOGIC ERROR: No zero division check
        result = a / b
        return result
    
    def complex_calculation(self, numbers):
        # PERFORMANCE ERROR: Nested loops O(n³)
        results = []
        for i in numbers:
            for j in numbers:
                for k in numbers:
                    # PERFORMANCE ERROR: String concatenation in loop
                    output = ""
                    output += str(i * j * k)
                    results.append(output)
        return results
    
    def factorial(self, n):
        if n == 0:
            return 1
        else:
            # LOGIC ERROR: No input validation for negative numbers
            return n * self.factorial(n - 1)
    
    def unused_function(self):
        # LOGIC ERROR: Unused variable
        unused_variable = "This is never used"
        temporary_value = 42
        return "Hello"
    
    def infinite_loop_demo(self):
        # LOGIC ERROR: Infinite loop
        while True:
            print("This will run forever!")
            time.sleep(1)
    
    def process_data(self, data_list):
        # TODO: Implement data processing
        # FIXME: This function is incomplete
        pass

# SYNTAX ERROR: Function definition without colon
def broken_function()
    return "This won't work"

# Global variable (performance issue)
global_counter = 0

def increment_global():
    global global_counter
    global_counter += 1
    return global_counter
