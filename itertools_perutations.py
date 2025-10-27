import itertools as it

permutations = list(it.permutations(['a', 'b', 'c']))
print(permutations)

#To make it more clear, here is a real world example
# Finding the best delivery route for a delivery truck that has to visit 4 cities

cities = ['Tokyo', 'Osaka', 'Hokaido', 'Hueno']

distances = {
    ('Tokyo', 'Osaka'): 500,
    ('Tokyo', 'Hokaido'): 800,
    ('Tokyo', 'Hueno'): 300,
    ('Osaka', 'Hokaido'): 600,
    ('Osaka', 'Hueno'): 400,
    ('Hokaido', 'Hueno'): 700
}

def route_distance(route):
    total = 0
    for i in range(len(route)-1):
        a, b = route[i], route[i+1]
        total += distances.get((a,b)) or distances.get((b, a))
    return total

best_route = None
shortest_distance = float('inf')
permuted_cities = []


for route in it.permutations(cities):
    d = route_distance(route)
    permuted_cities.append(route)
    if d < shortest_distance:
        shortest_distance = d
        best_route = route

print(f'Best route: {best_route} with distance {shortest_distance} km')
print('Cities permutations')
print(permuted_cities)