# Example file for Advanced Python by Joe Marini
# Demonstrate how to use list comprehensions

temps = [32, 65, 104, 212]


def fToC(val: float):
    return val * 9 / 5 + 32


print(list(map(fToC, temps)))
# define two lists of numbers
evens = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
odds = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]

# Perform a mapping and filter function on a list using built-in functions
print(list(map(lambda a: a**2, filter(lambda a: a > 4 and a < 16, evens))))

# Derive a new list of numbers frm a given list
print([e**2 for e in evens])

# Limit the items operated on with a predicate condition
print([e**2 for e in odds if e > 3 and e < 17])
