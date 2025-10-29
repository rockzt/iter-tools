import itertools as it
import operator
from copy import deepcopy

# First order sequence relations

five_ones = it.repeat(1, 5)
three_fours = it.repeat(4, 3)

print('Five ones:', list(five_ones))
print('Three fours:', list(three_fours))

# You can also use cycle to create an infinite repeating pattern
alternating_pattern = it.cycle([1, -1])
print('First 10 elements of alternating pattern:', [next(alternating_pattern) for _ in range(10)])


# The real goal is to produce a single function that can generate any first order recurrence relation
# One way to do this is using itertools.accumulate()
# This one takes two arguments - an iterable inputs and a binary function
# Then returns an iterator that over accumulated results for applying func to elements of inputs

def accumulated(inputs, func):
    itr = iter(inputs)
    prev = next(itr)
    for cur in itr:
        yield prev
        prev = func(prev, cur)

# Cumulative sum example
nums = [1, 2, 3, 4, 5]
list(accumulated(nums, lambda a, b: a + b))
'''
Printing the steps:

prev=1, cur=2 → yield 1, then prev=3
prev=3, cur=3 → yield 3, then prev=6
prev=6, cur=4 → yield 6, then prev=10
prev=10, cur=5 → yield 10, then prev=15
'''

# Cumulative product example
nums = [2, 4, 6, 8, 10, 12]
list(accumulated(nums, lambda a, b: a * b))
'''
Printing the steps:

prev=2, cur=4 → yield 2, then prev=8
prev=8, cur=6 → yield 8, then prev=48
prev=48, cur=8 → yield 48, then prev= 384
prev=384, cur=10 → yield 384, then prev= 3840
prev=3840, cur=12 → yield 30 , then prev= 46080
'''

# Tracking running maximum
nums = [5, 3, 8, 2, 7]
list(accumulated(nums, lambda a, b: max(a, b)))
'''
Printing the steps:

prev=5, cur=3 → yield 5 , then prev= 5
prev=5, cur=8 → yield 5, then prev= 8
prev=8, cur=2 → yield 8, then prev= 8 
prev=8, cur=7 → yield 8, then prev= 8
'''

#To make this more simple and represent the cumulative sum example lets improve the function
list_cumulative_sum = list(it.accumulate([1,2,3,4,5], operator.add))
print(list_cumulative_sum)

# More examples to get you familiar with accumulate
list_cumulative_min = list(it.accumulate([9, 21, 17, 5, 11, 12, 2, 6], min))  # Cumulative product
print(list_cumulative_min)

# Using more complex functions like lamda expressions that can be passed to accumulate
list_cumulative_lambda = list(it.accumulate([1, 2, 3, 4, 5],lambda x, y: (x + y) / 2))
print(list_cumulative_lambda)

# Now in order for accumulate to iterate over the resulting recurrence relation, you need to pass it
# to an infinite sequence with the right initial value.
def first_order(p, q, initial_val):
    # Returning sequence defined by by s(n) = p * s(n-1) + q.
    return it.accumulate(it.repeat(initial_val), lambda s, _: p*s + q)

# Now it's time to test our function with some real examples
# First let's generate the sequence of even numbers
evens = first_order(1, 2,0)
evens_list = list(next(evens) for _ in range(5))  # First 5 even numbers
print(evens_list)
'''
Printing the steps:
[0,0,0,0,0]
prev=0, cur=0 → yield 0, then prev=2
prev=2, cur=0 → yield 2, then prev=4
prev=4, cur=0 → yield 4, then prev= 6
prev=6, cur=0 → yield 6, then prev= 8
prev=8, cur=0 → yield 8 , then prev= 10
'''




#  Now let's generate the sequence of odd numbers
odds = first_order(1, 2, 1)
odds_list = list(next(odds) for _ in range(5))  # First 5 odd numbers
print(odds_list)
'''
Printing the steps:
[1,1,1,1,1]
prev=1, cur=1 → yield 1 , then prev= 3 
prev=3, cur=1 → yield 3, then prev= 5 
prev=5, cur=1 → yield 5, then prev= 7 
prev=7, cur=1 → yield 7, then prev= 9
prev=9, cur=1 → yield 9 , then prev= 11
'''

# As a final example let's generate the sequence of alternating ones and negative ones
alternating_ones = first_order(-1, 0, 1)
alternating_list = list(next(alternating_ones) for _ in range(5))  # First 5 elements
print(alternating_list)
'''
Printing the steps:
[1,1,1,1,1]
prev=1, cur=1 → yield 1 , then prev= -1 
prev=-1, cur=1 → yield -1, then prev= 1 
prev=1, cur=1 → yield 1, then prev= -1
prev=-1, cur=1 → yield -1, then prev= 1
prev=1, cur=1 → yield -1 , then prev= -1
'''

# Now it's time to use a real file example
# Every order moves through various stages (PENDING → PAID → SHIPPED → DELIVERED)
# The next state depends only on the previous one

def next_step(current):
    state = {
        "PENDING": "PAID",
        "PAID": "SHIPPED",
        "SHIPPED": "DELIVERED",
        "DELIVERED": "DELIVERED",
    }
    print('Current state:', current, '-> Next state:', state.get(current, "PENDING"))
    return state.get(current, "PENDING")

def update_order(order):
    order = deepcopy(order) # To avoid mutating the original order
    order['status'] = next_step(order['status'])
    return order

# Calling update_order repeatedly to simulate order progression
initial_order = {'id': 1, 'status': 'PENDING'}
order_progression = it.accumulate(it.repeat(initial_order), lambda order, _: update_order(order))
# Printing the order status progression
print('Real world example of order progression -  Simulating order status updates')
print(list(next(order_progression) for _ in range(5)))  # Simulate 5 updates
