# Common interview style problem using itertools
'''
You have three $20 dollar bills, five $10 dollar bills, two $5 dollar bills, and five $1 dollar bills.
How many different ways can you make $100 using any combination of these bills?
'''

import itertools as it
bills = [1,1,1,1,1,5,5,10,10,10,10,10,20,20,20]

# it.combinations() takes two arguments - an iterable and r (length of each combination)
# In his example we are listing the possible combinations of 3 bills from the  available bills
lis_of_combinations = list(it.combinations(bills,3))
print(f'Possible combinations of 3 bills: {len(lis_of_combinations)}')

#To find all combinations of bills that sum to 100 we need to do some more work
makes_100 = []
makes_50 = []

#  The counter starts from 1 because combinations of length 0 will always sum to 0
for i in range(1, len(bills)+1):
    for combo in it.combinations(bills, i):
        if sum(combo) == 100:
            makes_100.append(combo)

print(f'Makes 100 combinations: {len(makes_100)}')
print(makes_100)

print('-------------------------------')

for i in range(1, len(bills)+1):
    for combo in it.combinations(bills, i):
        if sum(combo) == 50:
            makes_50.append(combo)
print(f'Makes 50 combinations: {len(makes_50)}')
print(makes_50)
# So far so good, but we have a problem here - the same combination can appear multiple times
# To avoid this we can use set to store only unique combinations
unique_50 = set(makes_50)
unique_100 = set(makes_100)


print('----PRINTING UNIQUE COMBINATIONS ONLY----')
print(f'Unique makes 100 combinations: {len(unique_100)}')
print(unique_100)
print(f'Unique makes 50 combinations: {len(unique_50)}')
print(unique_50)

# Here is a variation using combinations_with_replacement, it just works like combinations but
# allows the same element to be chosen multiple times in a combination
print('----COMBINATIONS WITH REPLACEMENT EXAMPLE----')
# Example: Combinations of 2 bills allowing replacement
combinations_two_bills  = list(it.combinations_with_replacement([1,2],2))
print('Using combinations_with_replacement()')
print(combinations_two_bills)

combinations_two_bills_no_replacement  = list(it.combinations([1,2],2))
print('Using combinations()')
print(combinations_two_bills_no_replacement)

# Applying this new method to our original problem allows to avoid using set to filter unique combinations
bills = [50, 20, 10, 5, 1]
makes_100_no_duplicates = []

for i in range(1,  101):
    for combo in it.combinations_with_replacement(bills, i):
        if sum(combo) == 100:
            makes_100_no_duplicates.append(combo)
print('----PRINTING UNIQUE COMBINATIONS USING combinations_with_replacement()----')
print(f'Makes 100 combinations without duplicates: {len(makes_100_no_duplicates)}')
