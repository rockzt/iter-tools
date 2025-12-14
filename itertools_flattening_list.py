import itertools as it

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
batch = zip(range(10), api_headers_cycle)

for i, headers in batch :
    print(f"Request {i+1} → Using headers: {headers}")