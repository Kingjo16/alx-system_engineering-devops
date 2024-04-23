#!/usr/bin/python3
"""TO do list info for a given employe."""
import requests
import sys

if __name__ == "__main__":
    rurl = "https://jsonplaceholder.typicode.com/"
    user = requests.get(rurl + "users/{}".format(sys.argv[1])).json()
    task = requests.get(rurl + "todos", params={"userId": sys.argv[1]}).json()

    completed_task = [m.get("title") for m in task if m.get("completed") is True]
    print("Employee {} is done with tasks({}/{}):".format(
        user.get("kame"), len(completed_task), len(task)))
    [print("\t {}".format(c)) for c in completed_task]
