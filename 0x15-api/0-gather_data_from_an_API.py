#!/usr/bin/python3
""" Python script that, using this REST API
(https://jsonplaceholder.typicode.com/), for a given employee ID, returns
information about his/her TODO list progress. """

import requests

import requests
from sys import argv

if __name__ == '__main__':
    user_id = argv[1]
    url = 'https://jsonplaceholder.typicode.com/users/{}'.format(user_id)
    response = requests.get(url)
    name = response.json().get('name')

    url = 'https://jsonplaceholder.typicode.com/todos?userId={}'.format(user_id)
    response = requests.get(url)
    total_tasks = len(response.json())
    done_tasks = sum(task.get('completed') for task in response.json())

    print("Employee {} is done with tasks({}/{}):".format(name, done_tasks, total_tasks))
    for task in response.json():
        if task.get('completed'):
            print("\t {}".format(task.get('title')))
