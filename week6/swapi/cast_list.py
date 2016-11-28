import requests
import json
import os.path


def get_all_people():
    filename = "swapi_cache_people.json"
    if os.path.isfile(filename):
        with open(filename, "r") as f:
            results = json.loads(f.read())
    else:
        url = "http://swapi.co/api/people/"
        r = requests.get(url)
        results = r.json()["results"]

        while r.json()["next"]:
            r = requests.get(r.json()["next"])
            results += r.json()["results"]

        with open(filename, "w") as f:
            f.write(json.dumps(results, indent=4))

    return results


def find_person(who, people):
    for person in people:
        if person["name"].lower() == who.lower():
            print(person["films"])


if __name__ == "__main__":
    people = get_all_people()
    find_person(input("who would you like to find? "), people)
