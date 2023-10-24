#!/usr/bin/python3
"""
Python script to export data in the CSV format.
"""
from sys import argv
import json
import requests


if __name__ == '__main__':
    url = 'https://jsonplaceholder.typicode.com/'

    user_endpoint = '{}users/{}'.format(url, argv[1])
    user_response = requests.get(user_endpoint)
    user_data = user_response.json()
    employee_name = user_data.get('username')

    todos_endpoint = '{}todos?userId={}'.format(url, argv[1])
    todos_response = requests.get(todos_endpoint)
    todos_data = todos_response.json()

    json_file_name = '{}.json'.format(argv[1])
    user_task = []
    for task in todos_data:
        task_data = {
            "task": task.get("title"),
            "completed": task.get("completed"),
            "username": employee_name
        }
        user_task.append(task_data)

    user_data_json = {str(argv[1]): user_task}

    with open(json_file_name, mode="w") as jsonfile:
        json.dump(user_data_json, jsonfile)
