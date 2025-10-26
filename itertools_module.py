# This module demonstrates the use of the zip function in Python.
output_list  = zip([1,2,3,4],['a','b','c','d'])
print(list(output_list))

# Using map to get lengths of strings in a list
output_len_map = list(map(len, ['apple', 'banana', 'cherry']))
print(output_len_map)

# Using map with zip to sum corresponding elements of two lists
output_list_map_sum = list(map(sum, zip([1,2,3],[4,5,6])))
print(output_list_map_sum)

# Naive grouper function to group elements from an iterable into fixed-length chunks
'''
def naive_grouper(inputs, n):
    num_groups = len(inputs) // n
    return [tuple(inputs[i*n:(i+1)*n]) for i in range(num_groups)]

for _ in naive_grouper(range(100000000), 10):
    pass
'''
'''
Run the following command to check memory usage when calling previous function: 
time -f "Memory used (kB): %M\nUser time (seconds): %U" python3 itertools_module.py (for shell cli)
/usr/bin/time -l python3 itertools_module.py (for bash cli on macOS)

As you can see we required around 4.5 gb of memory to process 100 million integers in chunks of 10.
'''

# Implementing iterators to reduce memory usage
'''
def better_grouper(inputs, n):
    iters = [iter(inputs)] * n
    return zip(*iters)

for _ in better_grouper(range(100000000), 10):
    pass
'''
# Now the memory usage is significantly reduced to just a few MBs.

# But you can improve it further using itertools
# Dummy example to show usage of itertools.zip_longest
import itertools as it
x = [1,2,3,4,5]
y = ['a','b','c']
print(list(zip(x,y))) # Misses the last two elements of x
print(list(it.zip_longest(x,y))) # fill up with None by default when missing elements of either iterable

# Real world example of itertools.zip_longest
import itertools as it
def grouper(inputs, n, fillvalue=None):
    iters = [iter(inputs)] * n
    return it.zip_longest(iters, fillvalue=fillvalue)

for _ in grouper(range(100000003), 10,):
    pass
'''
Run the following command to check memory usage when calling previous function:
/usr/bin/time -l python3 itertools_module.py (for bash cli on macOS)
With this minor modification you keep the memory usage low and also handle the leftover elements
'''

if __name__ == "__main__":
    pass