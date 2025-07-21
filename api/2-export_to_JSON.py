#!/usr/bin/python3
"""Exports TODO list data for a given employee ID to JSON format."""

import json
import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./2-export_to_JSON.py <employee_id>")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print("Employee ID must be an integer.")
        sys.exit(1)

    # Fetch user data
    user_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    user_response = requests.get(user_url)
    if user_response.status_code != 200:
        print("User not found.")
        sys.exit(1)

    user = user_response.json()
    username = user.get("username")

    # Fetch todos for that user
    todos_url = f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"
    todos_response = requests.get(todos_url)
    todos = todos_response.json()

    # Build the required JSON structure
    task_list = []
    for task in todos:
        task_dict = {
            "task": task.get("title"),
            "completed": task.get("completed"),
            "username": username
        }
        task_list.append(task_dict)

    data = {str(employee_id): task_list}

    # Write to JSON file
    file_name = f"{employee_id}.json"
    with open(file_name, "w", encoding='utf-8') as jsonfile:
        json.dump(data, jsonfile)

