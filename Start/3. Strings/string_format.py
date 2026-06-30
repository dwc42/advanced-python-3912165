# Example file for Advanced Python by Joe Marini
# Formatting output strings
import itertools

# Basic formatting - center(), ljust(), rjust()
print("center".center(40, "-"))
print("ljust".ljust(40, "-"))
print("rjust".rjust(40, "-"))
# Formatting strings with format specification codes
# Format spec is: [[fill]align][sign]["z"]["#"]["0"][width][grouping_option]["."precision][type]
val1 = 1234.5678
val2 = 10987.65
val3 = 12.99
val4 = -280.7


# Specify a precision and type
print(f"{val1:.2f}")
print(f"{val2:.2f}")
print(f"{val3:.2e}")
print(f"{val4:.2e}")


# Use alignment and width and leading zeros
# < is left align, > is right align, ^ is centered

print(f"{val1:>10.2f}")
print(f"{val2:<10.2f}")
print(f"{val3:^10.2e}")
print(f"{val4:.2e}")
# Use a grouping option and +/- signs
print(f"{val1:_>-10,.2f}")
print(f"{val2:_<-10,.2f}")
print(f"{val3:^+10,.2e}")
print(f"{val4:+,.2e}")

# Insert a fill character


# Create format specifiers dynamically
width = 30
precision = 2
formatSpec = f"{val2:>{width}.{precision}f}"
print(formatSpec),
import string
import functools


def process_string(the_str: str, term: str):
    found = the_str.lower().find(term.lower())
    return {
        "Lowercase": functools.reduce(
            lambda s, c: s + 1 if c in string.ascii_lowercase else s, the_str, 0
        ),
        "Uppercase": functools.reduce(
            lambda s, c: s + 1 if c in string.ascii_uppercase else s, the_str, 0
        ),
        "Punctuation": functools.reduce(
            lambda s, c: s + 1 if c in string.punctuation else s, the_str, 0
        ),
        "Whitespace": functools.reduce(
            lambda s, c: s + 1 if c in string.whitespace else s, the_str, 0
        ),
        "Found": found > -1,
        "Index": found,
    }
