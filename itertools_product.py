# Creating a deck of cards using a generator function
from copy import deepcopy

ranks = ['A', 'K', 'Q', 'J', '10', '9', '8', '7', '6', '5', '4', '3', '2']
suits = ['H','D','C','S']

def cards():
    for rank in ranks:
        for  suit in suits:
            yield rank, suit

deck_of_cards = list(cards())


# Meke it simple using generator expression
cards = ((rank,suit) for rank in ranks for suit  in suits)


                    #Using itertools.product to achieve the same result
import itertools as it
deck_of_cards_itertools = it.product(ranks, suits)


#Now we need to shuffle the deck first before dealing
import random

def shuffle_deck(deck):
    """Return iterator over shuffled deck."""
    deck = list(deck)
    random.shuffle(deck)
    return iter(tuple(deck))


shuffled_deck  = shuffle_deck(deck_of_cards_itertools)

print_shuffle_deck = deepcopy(shuffled_deck)
print('Printing shuffled deck of cards:')
print(list(print_shuffle_deck))

# Now let's say you want to allow your users to cut the deck at a specific position - NO THE BEST OPTION
def cut(deck, position):
    """Return an itertor over a deck of cards cut at index 'position'."""
    # Check position is a valid integer
    if  not isinstance(position, int) or position <0:
        raise ValueError('Position must be a non-negative integer')

    deck = list(deck)
    return iter(deck[position:] + deck[:position])

cards_cut = cut(shuffled_deck, 10)
print('Printing cut deck of cards at position 10:')
print(list(cards_cut))

# Now let use itertools.islice, itertools.tee and itertools.chain to deal cards from the deck - BEST OPTION
# In this way we avoid memory overhead of creating new lists


# itertools.tee creates two independent iterators from a single original iterator
# be careful when using tee with large iterators as it can lead to high memory usage
iterator1 , iterator2 = it.tee([1,2,3,4,5], 2)
print(list(iterator1))
print(list(iterator2))


# itertools.islice works much like slicing a list but works with iterators
# You pass an iterable, a starting and stopping position and just like slicing a list
# it returns an iterator over the specified range
# You can optionally include a step argument as well.
# The biggest difference here is that slice returns an iterator instead of a list
list_sliced = it.islice('ABCDEFG', 2, 5)
print(list(list_sliced))

# slice from beginning to position 4, in steps of 2
list_sliced = it.islice([1,2,3,4,5,6,7,8,9], 0, 5, 2)
print(list(list_sliced))

# Slice from beginning to index 3
list_sliced = it.islice('ABCDEFG', 4)
print(list(list_sliced))

# itertools.chain this function takes any number of iterables as arguments and "chains" them together
list_chained = it.chain('ABCDEFG',[1,2,3,4,5])
print(list(list_chained))


# Now you can reimplement the cut function using iterttols




def itertools_cut(deck, position):
    pass