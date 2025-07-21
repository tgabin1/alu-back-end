#!/usr/bin/python3
"""
Displays the TODO list progress of an employee using a REST API.
"""

import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./todo_progress.py <employee_id>")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print("Employee ID must be an integer.")
        sys.exit(1)

    # Fetch employee data
    user_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    user_response = requests.get(user_url)
    if user_response.status_code != 200:
        print("User not found.")
        sys.exit(1)
    user = user_response.json()
    employee_name = user.get("name")

    # Fetch todos for the employee
    todos_url = f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"
    todos_response = requests.get(todos_url)
    todos = todos_response.json()

    # Filter completed tasks
    completed_tasks = [task for task in todos if task.get("completed")]
    total_tasks = len(todos)
    num_completed = len(completed_tasks)

    # Print the progress
    print(f"Employee {employee_name} is done with tasks({num_completed}/{total_tasks}):")
    for task in completed_tasks:
        print(f"\t {task.get('title')}")


