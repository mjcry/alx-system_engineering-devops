#!/usr/bin/python3
"""
Write a Python script that, using this REST API,
for a given employee ID, returns information about
his/her TODO list progress
export data in the CSV format.
"""

import csv
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
    username = res.json().get("username")

    url_task = "https://jsonplaceholder.typicode.com/todos"
    res_task = requests.get(url_task, params={"userId": id_c})
    if res_task.status_code != 200:
        print("Tasks not found")
        sys.exit(1)

    with open("{}.csv".format(id_c), "w") as file_c:
        writer = csv.writer(file_c, quoting=csv.QUOTE_ALL)
        writer.writerow(["employee_id", "username", "completed", "title"])
        for task in res_task.json():
            writer.writerow([id_c, username, task.get("completed"), task.get("title")])

