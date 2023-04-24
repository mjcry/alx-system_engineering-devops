#!/usr/bin/python3
"""
Write a  Python script that, using this REST API,
for a given employee ID, returns information about
his/her TODO list progress
"""

import requests
import sys


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: {} employee_id".format(sys.argv[0]))
        sys.exit(1)

    id_c = sys.argv[1]
    url_user = "https://jsonplaceholder.typicode.com/users/{}".format(id_c)
    res = requests.get(url_user)
    if res.status_code != 200:
        print("User not found")
        sys.exit(1)
    name = res.json().get('name')

    url_task = "https://jsonplaceholder.typicode.com/todos"
    res_task = requests.get(url_task, params={"userId": id_c})
    if res_task.status_code != 200:
        print("Tasks not found")
        sys.exit(1)

    task_title = []
    complete = 0
    total_task = len(res_task.json())

    for task in res_task.json():
        if task.get('completed'):
            task_title.append(task['title'])
            complete += 1

    print("Employee {} is done with tasks({}/{}):".format(name, complete, total_task))
    for title in task_title:
        print("\t{}".format(title))

