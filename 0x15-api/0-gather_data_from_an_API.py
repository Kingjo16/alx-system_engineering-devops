#!/usr/bin/python3
"""TO do list info for a given employe."""
import re
import requests
import sys

REST_API = "https://jsonplaceholder.typicode.com"

if __name__ == '__main__':
    if len(sys.argv) > 1:
        if re.fullmatch(r'\d+', sys.argv[1]):
            id = int(sys.argv[1])
            url_req = requests.get('{}/users/{}'.format(REST_API, id)).json()
            task = requests.get('{}/todos'.format(REST_API)).json()
            user = url_req.get('name')
            todo = list(filter(lambda x: x.get('userId') == id, task))
            completed = list(filter(lambda x: x.get('completed'), todo))
            print(
                'Employee {} is done with tasks({}/{}):'.format(
                    user,
                    len(completed),
                    len(todo)
                )
            )
            if len(completed) > 0:
                for t in completed:
                    print('\t {}'.format(t.get('title')))
