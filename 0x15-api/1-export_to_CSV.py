#!/usr/bin/python3
"""
Python script to export data in the CSV format.
"""
from sys import argv
import csv
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

    with open('{}.csv'.format(argv[1]), mode='w') as csvfile:
        csv_writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for todo in todos_data:
            csv_writer.writerow([argv[1], employee_name,
                                todo.get('completed'), todo.get('title')])
