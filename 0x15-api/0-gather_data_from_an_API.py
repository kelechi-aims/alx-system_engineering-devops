#!/usr/bin/python3
"""
Script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress.
"""
import requests
from sys import argv


if __name__ == '__main__':
    url = 'https://jsonplaceholder.typicode.com/'

    user_endpoint = '{}users/{}'.format(url, argv[1])
    user_response = requests.get(user_endpoint)
    user_data = user_response.json()
    employee_name = user_data.get('name')

    todos_data = requests.get(url + "user/{}/todos".format(argv[1])).json()

    completed_tasks = []
    for task in todos_data:
        if task.get('completed'):
            completed_tasks.append(task)

    total_tasks = len(todos_data)

    completed_tasks_count = len(completed_tasks)

    print("Employee {} is done with tasks({}/{}):".format(
        employee_name, completed_tasks_count, total_tasks))

    for task in completed_tasks:
        print("\t {}".format(task.get("title")))
