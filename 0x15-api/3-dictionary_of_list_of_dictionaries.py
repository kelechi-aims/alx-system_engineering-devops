#!/usr/bin/python3
"""
Script that, using this REST API, gets information about TODO
list progress for all employees and exports it to a JSON file.
"""
import json
import requests

if __name__ == '__main__':
    url = 'https://jsonplaceholder.typicode.com/'

    users_response = requests.get(url + 'users')
    users_data = users_response.json()

    all_tasks = {}

    for user in users_data:
        user_id = user.get('id')
        username = user.get('username')

        todos_response = requests.get(url + f'todos?userId={user_id}')
        todos_data = todos_response.json()

        user_tasks = []
        for task in todos_data:
            task_data = {
                "username": username,
                "task": task.get("title"),
                "completed": task.get("completed")
            }
            user_tasks.append(task_data)

        all_tasks[str(user_id)] = user_tasks

    json_file_name = 'todo_all_employees.json'

    with open(json_file_name, 'w') as jsonfile:
        json.dump(all_tasks, jsonfile)
