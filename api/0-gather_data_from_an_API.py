#!/usr/bin/python3
"""
Fetches TODO list for a given employee ID and exports completed tasks to CSV.
"""
import requests
import sys
import csv

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./todo_progress.py <employee_id>")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print("Employee ID must be an integer.")
        sys.exit(1)

    # Fetch user info
    user_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    user_response = requests.get(user_url)
    if user_response.status_code != 200:
        print(f"No user found with ID {employee_id}")
        sys.exit(1)
    user = user_response.json()
    employee_name = user.get("name")

    # Fetch todos for the user
    todos_url = f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"
    todos_response = requests.get(todos_url)
    todos = todos_response.json()

    # Filter completed tasks
    completed_tasks = [task for task in todos if task.get("completed")]
    total_tasks = len(todos)
    num_completed = len(completed_tasks)

    # Display on terminal
    print(f"Employee {employee_name} is done with tasks({num_completed}/{total_tasks}):")
    for task in completed_tasks:
        print(f"\t {task.get('title')}")

    # Export to CSV
    filename = f"employee_{employee_id}.csv"
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        for task in todos:
            writer.writerow([
                employee_id,
                employee_name,
                str(task.get("completed")),
                task.get("title")
            ])

    print(f"\nData exported to {filename}")

