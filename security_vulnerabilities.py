"""
security_vulnerabilities.py - Code with security vulnerabilities
WARNING: This code contains intentional security vulnerabilities for testing
"""

import os
import sqlite3

# SECURITY ERROR: Hardcoded credentials
DATABASE_PASSWORD = "admin123"
API_KEY = "sk-1234567890abcdef"
SECRET_TOKEN = "super_secret_token_123"

class VulnerableUserManager:
    def __init__(self):
        self.db_connection = None
        self.admin_password = "password123"  # SECURITY: Hardcoded password
    
    def execute_user_query(self, user_input):
        # SECURITY ERROR: SQL Injection vulnerability
        query = "SELECT * FROM users WHERE name = '" + user_input + "'"
        return self.execute_sql(query)
    
    def execute_sql(self, query):
        # Simulate SQL execution
        print(f"Executing: {query}")
        return []
    
    def evaluate_expression(self, expression):
        # SECURITY ERROR: Use of eval() - code injection risk
        result = eval(expression)
        return result
    
    def execute_command(self, command):
        # SECURITY ERROR: Use of exec() - code execution risk
        exec(command)
    
    def update_user_data(self, user_id, field, value):
        # SECURITY ERROR: SQL injection in UPDATE
        update_query = f"UPDATE users SET {field} = '{value}' WHERE id = {user_id}"
        return self.execute_sql(update_query)
    
    def delete_user(self, username):
        # SECURITY ERROR: SQL injection in DELETE
        delete_query = "DELETE FROM users WHERE username = '" + username + "'"
        return self.execute_sql(delete_query)
    
    def login_user(self, username, password):
        # SECURITY ERROR: SQL injection in authentication
        auth_query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
        result = self.execute_sql(auth_query)
        return len(result) > 0

# SECURITY ERROR: Hardcoded database connection
def connect_to_database():
    connection_string = "mysql://admin:password123@localhost/mydb"
    return connection_string

# SECURITY ERROR: Unsafe file operations
def read_user_file(filename):
    # No path validation - directory traversal vulnerability
    with open(filename, 'r') as f:
        return f.read()
