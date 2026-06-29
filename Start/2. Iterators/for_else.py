# Example file for Advanced Python by Joe Marini
# The for-else loop construct

names = ["Jim", "Pam", "Creed", "Michael", "Dwight", "Oscar", "Kevin", "Phyllis"]

# The else clause on a for loop is only executed if the loop completes every iteration
# def findname(target):
#     for name in names:
#         if name == target:
#             print("Name found");
#             return True


#     print("Name not found")
#     return False
def findName(string: str):
    return bool(names.count(string))


print(findName("Joe"))
print(findName("Null"))
print(findName("Creed"))
print(findName("Tom"))


# Check if a number is prime
def isPrime(num: int):
    if num < 2:
        return True
    for i in range(2, int(num / 2) + 1):
        if not (num % i):
            return False
    else:
        return True


print(isPrime(37893))
print(isPrime(61))
print(isPrime(5))
