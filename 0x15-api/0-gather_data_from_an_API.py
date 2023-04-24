#!/usr/bin/python3
"""
Module to get todo list progress of an employee from https://jsonplaceholder.typicode.com/.
"""
import sys
import requests


def get_todo_list(employee_id):
    """
    Function to get the employee TODO list progress.
    """
    # API endpoint for getting employee details
    employee_url = 'https://jsonplaceholder.typicode.com/users/{}'.format(employee_id)
    # API endpoint for getting employee's tasks
    tasks_url = 'https://jsonplaceholder.typicode.com/todos?userId={}'.format(employee_id)

    # Fetching employee details
    response = requests.get(employee_url)
    employee = response.json()
    name = employee.get('name')

    # Fetching employee's tasks
    response = requests.get(tasks_url)
    tasks = response.json()
    total_tasks = len(tasks)
    completed_tasks = [task for task in tasks if task.get('completed')]
    num_completed_tasks = len(completed_tasks)

    # Outputting results
    print("Employee {} is done with tasks({}/{}):".format(name, num_completed_tasks, total_tasks))
    for task in completed_tasks:
        print("\t {} {}".format(task.get('title'), '\t'))

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: {} EMPLOYEE_ID".format(sys.argv[0]))
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print("Employee ID must be an integer")
        sys.exit(1)

    get_todo_list(employee_id)


