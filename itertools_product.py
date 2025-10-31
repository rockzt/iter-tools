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


# slice from beginning to position 4, in steps of 2
list_sliced = it.islice([1,2,3,4,5,6,7,8,9], 0, 5, 2)

# Slice from beginning to index 3
list_sliced = it.islice('ABCDEFG', 4)



# itertools.chain this function takes any number of iterables as arguments and "chains" them together
list_chained = it.chain('ABCDEFG',[1,2,3,4,5])



# Now you can reimplement the cut function using iterttols using itertools.islice, itertools.tee and itertools.chain
def itertools_cut(deck, position):
    deck1 , deck2 = it.tee(deck, 2)
    top = it.islice(deck1, position)
    bottom = it.islice(deck2, position, None)
    return it.chain(bottom, top)

#Creating a new deck of cards using itertools.product
deck_of_cards_itertools = it.product(ranks, suits)

cards_itertools_curt = itertools_cut(deck_of_cards_itertools, 10)
#print('Printing cut deck of cards at position 10 using itertools:')
#print(list(cards_itertools_curt))


#Now as the final step let's deal cards from the deck
def deal(deck, number_of_hands, cards_per_hand):
    """Return a tuples of hands dealt from the deck."""
    iters = [iter(deck)] * cards_per_hand
    return tuple(zip(*(tuple(it.islice(itr, number_of_hands)) for itr in iters)))


hand_1, hand_2, hand_3 = deal(cards_itertools_curt, 3, 7)
print('Dealt hands:')
print('Hand 1:', hand_1)
print('Hand 2:', hand_2)
print('Hand 3:', hand_3)

print('Length of the deck after dealing hands:', len(list(cards_itertools_curt)))  # Should be 52 - (3*7) = 31