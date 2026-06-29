# Example file for Advanced Python by Joe Marini
# Using special module names
import collections

# __name__ is the name of the module
print("__name__",__name__)

# __file__ contains the path to the file from which the module was loaded
print("__file__",__file__)

# __package__ indicates the package that the module belongs to.
print("__package__",__package__)
print("collections", collections.__package__)
if (__name__ == "__main__"):
	print("code ran directly")
