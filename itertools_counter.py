import itertools as it

# Using itertools.count to generate an infinite sequence of numbers
counter = it.count()
list_generated_by_count = list(next(counter) for _ in range(10))  # Generates numbers from 0 to 9
print(list_generated_by_count)

# Generating even numbers starting from 2
evens = it.count(step=2)
list_even_numbers= list(next(evens) for _ in range(6))
print(list_even_numbers)  # Generates first 5 even numbers starting from 2

# Generating odd numbers starting from 1
odds = it.count(start=1, step=2)
list_odd_numbers = list(next(odds) for _ in range(5))
print(list_odd_numbers)  # Generates first 5 odd numbers starting from 1


# Ever since Python 3.1 itertools.count supports float and Decimal types
counting_with_flows = it.count(start=0.5, step=0.5)
list_counting_with_floats = list(next(counting_with_flows) for _ in range(5))
print(list_counting_with_floats)

# You can even pass negative arguments
counting_with_negatives = it.count(start=-1, step=-0.3)
list_counting_with_negatives = list(next(counting_with_negatives) for _ in range(5))
print(list_counting_with_negatives)

# A common more useful example is to enumerate a list
# without needing to use a for loop
enumerated_list = list(zip(it.count(), ['apple', 'banana', 'cherry']))
print('Enumerated list using itertools.count():')
print(enumerated_list)

# Using a more real world example,let say we want to assign unique IDs to a list of users
# When exporting data to a CSV file, you often want an auto-increment cloumn like index
import csv

data = [
    {"name": "Alice", "score": 85},
    {"name": "Bob", "score": 92},
    {"name": "Carol", "score": 78}
]

with open('score.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['ID', 'Name', 'Score'])  # Writing header
    for user_id, entry in zip(it.count(1), data):
        writer.writerow([user_id, entry['name'], entry['score']])