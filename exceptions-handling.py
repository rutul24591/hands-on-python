# Exception Handling
# Done using try/except block


def do_some_stuff_with_number(a):
    print(a)


def main():
    list = [1, 2, 3, 4, 5]

    for i in range(20):
        try:
            do_some_stuff_with_number(list[i])
        except:
            do_some_stuff_with_number(
                0
            )  # Raised when accessing a non-existing index of a list


main()

"""
Exercise

# Setup
actor = {"name": "John Cleese", "rank": "awesome"}


# Function to modify!!!
def get_last_name():
    return actor["name"].split()[1]


# Test code
get_last_name()
print("All exceptions caught! Good job!")
print("The actor's last name is %s" % get_last_name())

"""

actor = {"name": "John Cleese", "rank": "awesome"}


def get_last_name():
    return actor["name"].split()[1]


get_last_name()
print("All exceptions caught! Good job!")
print("The actor's last name is %s" % get_last_name())
