# Example file for Advanced Python by Joe Marini
# Sequences and slicing

from collections import deque

names = ["Jim", "Pam", "Creed", "Michael", "Dwight", "Oscar", "Kevin", "Phyllis"]

# a slice is a subset of a sequence. The form is [start:stop:step]
print(names[1:4])

# using a step
print(names[1:4:2])

# shorthand
print(names[:3])
print(names[5:])
print(names[::2])

# reversing with step of -1

print(names[::-1])
# assigning sequences
newNames = ["Andy", "Stanley", "Angela"]
names[2:4] = newNames
print(names)
# the del operator works with slices
del names[0:2]
print(names)
# not all sequence types support slicing, however
deque_names = deque(
    ["Jim", "Pam", "Creed", "Michael", "Dwight", "Oscar", "Kevin", "Phyllis"]
)
for name in deque_names:
    print(name)
print(len(deque_names))
