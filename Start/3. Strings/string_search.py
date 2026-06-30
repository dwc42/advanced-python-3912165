# Example file for Advanced Python by Joe Marini


sample_text = "The quick brown fox jumps over the lazy dog."

# Using find() to find the first occurrence of a substring
print(sample_text.find("the"))

# Example with optional start and end parameters
print(sample_text.find("fax", 5, 36))
# Using index() to find the first occurrence of a substring (raises ValueError if not found)
try:
    print(sample_text.index("fax"))
except ValueError:
    print("not found")

# The 'in' operator can be used for Boolean testing:
print("fox" in sample_text)

# Using rfind() to find the last occurrence of a substring
print(sample_text.rfind("the"))

# Using rindex() to find the last occurrence of a substring (raises ValueError if not found)

print(sample_text.rindex("the"))
# The replace() function will find content in the string and replace it
print(sample_text.replace("lazy", "tired"))
