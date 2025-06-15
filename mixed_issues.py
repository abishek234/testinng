"""
mixed_issues.py - A comprehensive test file with multiple issue types
This file tests all capabilities of the AI Swarm Code Analyzer
"""

import os
import sys
import json

# SECURITY: Hardcoded API credentials
OPENAI_API_KEY = "sk-abcd1234567890"
DATABASE_URL = "postgresql://user:pass123@localhost/db"
JWT_SECRET = "my_super_secret_key_123"

class DataProcessor:
    def __init__(self, config_file):
        # LOGIC ERROR: No file existence check
        with open(config_file, 'r') as f:
            self.config = json.load(f)
        
        # LOGIC ERROR: Unused variables
        unused_variable = "This is never used"
        temp_data = [1, 2, 3, 4, 5]
        
    def process_data(self, data_list)  # SYNTAX ERROR: Missing colon
        """Process data with multiple issues"""
        results = []
        
        # PERFORMANCE ERROR: Nested loops O(n²)
        for i in range(len(data_list)):
            for j in range(len(data_list)):
                # PERFORMANCE ERROR: String concatenation in loop
                output = ""
                output += str(data_list[i])
                output += "-"
                output += str(data_list[j])
                results.append(output)
        
        return results
    
    def execute_user_command(self, command):
        # SECURITY ERROR: Command injection vulnerability
        result = eval(command)  # SECURITY: eval usage
        return result
    
    def query_database(self, user_input):
        # SECURITY ERROR: SQL injection
        query = f"SELECT * FROM data WHERE name = '{user_input}'"
        # Simulate database query
        print(f"Executing: {query}")
        return []
    
    def calculate_division(self, a, b):
        # LOGIC ERROR: No zero division check
        return a / b
    
    def infinite_processor(self):
        # LOGIC ERROR: Infinite loop
        while True:
            self.process_data([1, 2, 3])
            # No break condition
    
    def validate_email(self, email):
        # LOGIC ERROR: Insufficient validation
        if "@" in email:
            return True
        return False
    
    def process_passwords(self, password):
        # SECURITY ERROR: Hardcoded password comparison
        admin_password = "admin123"
        if password == admin_password:
            return True
        return False

# SYNTAX ERROR: Function without colon
def broken_function()
    return "This won't compile"

# Global variable usage (performance concern)
global_cache = {}

def cache_data(key, value):
    global global_cache
    global_cache[key] = value

# TODO: Implement proper error handling
# FIXME: This function needs optimization
def risky_file_operation(filename):
    # SECURITY ERROR: No path validation - directory traversal risk
    with open(filename, 'w') as f:
        f.write("Potentially dangerous file operation")

def dangerous_eval_usage(user_code):
    # SECURITY ERROR: Direct eval of user input
    exec(user_code)
    
def sql_injection_example(username):
    # SECURITY ERROR: SQL injection vulnerability
    query = "DELETE FROM users WHERE username = '" + username + "'"
    return query
