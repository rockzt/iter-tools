import itertools as it
from itertools import takewhile

# Creating flattening providing a single iterable as an argument
output_flatten_list = list(it.chain.from_iterable([[1,2,3,4,5],[6,7,8,9,10]]))
print(output_flatten_list)

# There is no reason the argument provided needs to be finite, you could emulate the behaviour of cycle()
# it.repeat('abc')  -> ['abc'] ['abc'] ['abc'] ['abc'] ...
# chain.from.iterable -> flattens each string one after another -> a, b, c, a, b, c, a, b, c, ...
cycle = it.chain.from_iterable(it.repeat('abc'))
# islice safely limits the output we want to get, in this case, we only want to get the first 20 elements
# So the output should look something like this -> ['a', 'b', 'c', 'a', 'b', 'c', 'a', 'b', 'c', 'a', 'b', 'c', 'a', 'b', 'c', 'a', 'b', 'c', 'a', 'b']
output_flatten_list_cycle = list(it.islice(cycle, 20))
print(output_flatten_list_cycle)

# Mental Model of the previous exercise
# Think of this as:
# repeat('abc')        →  ['abc'] ['abc'] ['abc'] ...
# chain.from_iterable  →   a b c   a b c   a b c
# islice(20)           →   take only first 20

# Real world examples
# - Simulating round-robin scheduling
# - Generating repeating API test data
# - Cycling through rate-limiting buckets
# - Streaming repeated patterns without loading them into memory

# Hands on real world example
# Each API key has multiple headers (iterables inside an iterable)
api_key_batches = [
    {"Authorization": "Bearer KEY_1", "Client": "A"},
    {"Authorization": "Bearer KEY_2", "Client": "B"},
    {"Authorization": "Bearer KEY_3", "Client": "C"},
]

# Create an infinite flattened stream of headers
api_headers_cycle = it.chain.from_iterable(
    it.repeat(api_key_batches)
)

# Simulate making 10 API calls
#batch = zip(range(10), api_headers_cycle)

'''
for i, headers in batch :
    print(f"Request {i+1} → Using headers: {headers}")
'''
# Applying itertools to real world example
# Analysing the S&P 500

from collections import namedtuple

class DataPoint(namedtuple('DataPoint', ['date','value'])):
    __slots__ = ()

    def __le__(self, other):
        return self.value <= other.value

    def __lt__(self, other):
        return self.value < other.value

    def __gt__(self, other):
        return self.value > other.value

import csv
from datetime import datetime
def read_prices(csvfile, _strptime=datetime.strptime):
    counter = 1
    with open(csvfile) as infile:
        reader = csv.DictReader(infile)
        for row in reader:
            yield DataPoint(date=_strptime(row['Date'], '%Y-%m-%d').date(), value= float(row['Adj Close']))

# Read prices and calculate daily percent change
prices = tuple(read_prices('csv/SP500.csv'))
gains = tuple(
    DataPoint(day.date, 100*(day.value/prev_day.value - 1.))
    for day, prev_day in zip(prices[1:], prices)
    )

# Determine Maximum Gain and Loss
'''
max_gain = DataPoint(None, 0)
print(max_gain)

for data_point in gains:
    max_gain = max(data_point, max_gain)
'''


# Alternative way to determine Maximum Gain and Loss using itertools.filterfalse() adn reduce together
# Even if there are never gains, you can handle this error by simple adding
# The reduce() function accepts an optional third argument for an initial value. Passing 0 to this third argument gets you the expected behavior
import functools as ft
# Find maximum daily gain/loss
zdp = DataPoint(None, 0)
#In this part you are telling it.filterfalse to remove those values that are equals or lower than Zero
'''
Compared to the example provided after the one down below, when calculating the gains, you do not have
to provide the zdp variable as an initializer due you are assuming there is at least one positive gain, 
if not, an exception is acceptable (or expected)
'''
max_gain = ft.reduce(
    max,
    it.filterfalse(lambda p: p <= zdp, gains)
)


# In this part you are telling it.filterfalse to remove those values that are greater than Zero.
# Inside the function reduce, we are adding an already declared empty variable that works as an initializer
# In this if the first value is empty the will not throw an error due the initializer provided
max_loss = ft.reduce(
    min,
    it.filterfalse(lambda p: p > zdp, gains), zdp
)


# Longest growth streak
# Using the itertools.takewhile() and itertools.dropwhile() functions
# it.takewhile(): takes a predicate and an iterable inputs as arguments and returns an ioterator over
# inputs that stops at the first instance of an element for which the predicate return False
# While the dropwhile() function does exactly the opposite. It returns an iterator beginning at the first
# element for which the predicate returns false

'''Examples Using it.takewhile()'''
#less_than = it.takewhile(lambda x: x < 3, [0,1,2,3,4])
#less_than = [value for value in less_than]
#print(less_than)

'''Examples Using it.dropwhile()'''
#greater_than = it.dropwhile(lambda x: x < 3, [0,1,2,3,4])
#greater_than = [value for value in greater_than]
#print(greater_than)

def consecutive_positives(sequence, zero=0):
    def _consecutives():
        for itr in it.repeat(iter(sequence)):
            yield tuple(it.takewhile(lambda p: p > zero,
                                     it.dropwhile(lambda p: p <= zero, itr)))
    return it.takewhile(lambda t: len(t), _consecutives())

# The function called returns an iterator with consecutive positive data points in gains
growth_streaks = consecutive_positives(gains, zero=DataPoint(None, 0))


# Now you can use reduce() to extrac the longest growth streak
longest_growth_streak = ft.reduce(lambda x, y: x if len(x) > len(y) else y, growth_streaks)

print(longest_growth_streak)








             # Exercise named tuple
'''
# Declaring namedtuple (first argment is the name of the new class and the second argument list of fields)
Student = namedtuple('Student' , ['name','age','DOB'])
# Adding values
new_values = Student('Rito','19','19178123')
# Accessing values by index
print(new_values[1])
# Accessing values by name
print(new_values.name)
# Accessing by getattr()
attribute_accessed = getattr(new_values, 'name')
print(attribute_accessed)
#---------------------------------------------------
    # Conversion Operations
# Using _make() return a namedtuple() from the iterable passed as argument
Student = namedtuple('Employee', ['nickname','code','speciality'])
S = Student('Rock','1517','recon')
print(S.nickname)
li = ['Nana','1983','None']
S1 = Student._make(li)
print(S1.nickname)

# Using _asdict() as constructed from the mapped values of namedtuple()
Student = namedtuple('Member',['name','age','range'])
S1 = Student('rockdrick','29','2')
print(S1.name)
S1_dict = S1._asdict()
print(S1_dict.get('name'))

# Using ** operator to convert a dictionary into the namedtuple().
Member = namedtuple('Member', ['name','age','code'])

M1 = Member('Momo','16','123457')
print(M1)
M2 = Member('Rito', '15', '13123')
print(M2)

#Creating a dictionary to be converted into the namedtuple
decoy_dict = {
    "name":"Yami",
    "age":"17",
    "code":"xxxxx"
}
print("Converting dict into namedtuple")
print(Member(**decoy_dict))
'''