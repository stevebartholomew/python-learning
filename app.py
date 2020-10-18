from store import load
from store import save

people = load()

for person in people:
    if person['name'] == 'Henry':
        person['number_of_sweets'] = person['number_of_sweets'] + 1

print(people)

save(people)
