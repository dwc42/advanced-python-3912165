# Example file for Advanced Python by Joe Marini
# Itertools: count, cycle, accumulate


import itertools

names = ["Joe", "Jane", "Jim"]


# cycle iterator can be used to cycle over a collection infinitely
cycle = itertools.cycle(names)
for i in range(0, 100):
    print(next(cycle))

# use count to create a simple counter
counter = itertools.count(100, 10)
for i in range(0, 10):
    print(next(counter))

# accumulate creates an iterator that accumulates values
vals = [10, 20, 30, 40, 50, 40, 30]
acc = itertools.accumulate(vals, max)
print(list(acc))

# amortize a loan over a set number of payments for a 2000 loan at 4%
payments = [100, 125, 200, 105, 100, 120, 110, 130, 150, 100, 110, 120]
balances = itertools.accumulate(
    payments, lambda bal, pay: round(bal * 1.04) - pay, initial=2000
)
print(list(balances))
