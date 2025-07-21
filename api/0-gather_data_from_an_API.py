#!/usr/bin/python3
import requests
import sys

if __name__ == "__main__":
    employee_id = int(sys.argv[1])

    # Get employee name
    user_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    user_data = requests.get(user_url).json()
    employee_name = user_data.get("name")

    # Get tasks
    todo_url = f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"
    todo_data = requests.get(todo_url).json()
    total_tasks = len(todo_data)
    done_tasks = [task for task in todo_data if task.get("completed")]

    print(f"Employee {employee_name} is done with tasks({len(done_tasks)}/{total_tasks}):")
    for task in done_tasks:
        print(f"\t {task.get('title')}")
