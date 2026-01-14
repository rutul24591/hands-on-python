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
