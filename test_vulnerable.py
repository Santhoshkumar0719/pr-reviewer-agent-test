
import subprocess
import sqlite3

# Vulnerability 1: Command Injection
def run_command(user_input):
    subprocess.run(user_input, shell=True)

# Vulnerability 2: Arbitrary Code Execution
def calculate(expression):
    return eval(expression)

# Vulnerability 3: Hardcoded Secret
API_KEY = "my-secret-api-key-12345"

# Vulnerability 4: SQL Injection
def get_user(cursor, user_id):
    query = f"SELECT * FROM users WHERE id = {user_id}"
    cursor.execute(query)

# Testing multiple vulnerabilities
