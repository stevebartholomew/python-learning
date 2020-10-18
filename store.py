import json

DATA_FILE = 'people.json'

def load():
    file = open(DATA_FILE)
    people = json.load(file)
    file.close()
    return people

def save(people):
    file = open(DATA_FILE, 'w')
    file.write(json.dumps(people))
    file.close()
    