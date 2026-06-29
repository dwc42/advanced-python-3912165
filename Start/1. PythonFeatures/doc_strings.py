# Example file for Advanced Python by Joe Marini
# Demonstrate the use of documentation strings


def myFunction(arg1, arg2=None):
    """Print Wrapper

    :param arg1: _description_
    :type arg1: Any
    :param arg2: _description_, defaults to None
    :type arg2: Any, optional
    """
    print(arg1, arg2)


def main():
    print(myFunction.__doc__)


if __name__ == "__main__":
    main()
