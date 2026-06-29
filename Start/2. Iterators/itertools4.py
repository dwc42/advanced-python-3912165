# Example file for Advanced Python by Joe Marini
# Itertools: combinations and permutations

import itertools

# product() produces the cartesian product of input iterables
cards = "A23456789TJQK"
suits = "SCHD"
print(list(itertools.product(cards, suits)))

# permutations() creates tuples of a given length with no repeated elements
teams = ("A", "B", "C", "D")
print(list(itertools.permutations(teams, 2)))

# combinations() will create combinations of a given length with no repeats
print(list(itertools.combinations(teams, 3)))


# combinations_with_replacement() will create combinations of a given length with repeats
print(list(itertools.combinations_with_replacement(teams, 3)))
