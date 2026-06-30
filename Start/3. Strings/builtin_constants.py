# Example file for Advanced Python by Joe Marini
# Using the built-in string constants

import string
import secrets

# built-in constants for a variety of needs
print(string.ascii_letters)
print(string.ascii_lowercase)
print(string.ascii_uppercase)
print(string.digits)
print(string.hexdigits)
print(string.punctuation)


# Define a test string
testStr = "The quick brown fox jumps OVER the lazy dog."
print(list(c in string.punctuation for c in testStr))
# use an iterator to see if a string contains any punctuation

if any(c in string.punctuation for c in testStr):
    print("punc")
else:
    print("no punc")

# generate a secure random password
aphabet = string.ascii_letters + string.digits + string.punctuation

print("".join(secrets.choice(aphabet) for i in range(10)))


# Check the strength of a password
def check_password_strength(testPass: str):
    return (
        len(testPass) >= 10
        and any(char in string.punctuation for char in testPass)
        and any(char in string.ascii_letters for char in testPass)
        and any(char in string.digits for char in testPass)
    )


print(check_password_strength("MyTestPa$$123!"))
print(check_password_strength("passwordisapasswoird1"))
print(check_password_strength("pa$$w0rd!"))
