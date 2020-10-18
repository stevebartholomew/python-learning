import json

DATA_FILE = 'people.json'

file = open(DATA_FILE)
people = json.load(file)
file.close()

for person in people:
    if person['name'] == 'Henry':
        person['number_of_sweets'] = person['number_of_sweets'] + 1 

print(people)

file = open(DATA_FILE, 'w')
file.write(json.dumps(people))
file.close()