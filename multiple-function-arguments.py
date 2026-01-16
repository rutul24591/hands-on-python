"""
Multiple Function Arguments
Every function in Python receives a predefined number of arguments, if declared normally, like this:

def myfunction(first, second, third):
    # do something with the 3 variables
    ...
"""


# It is possible to declare functions which receive a variable number of arguments, using the following syntax:
def foo(first, second, third, *therest):
    print("First: %s" % first)
    print("Second: %s" % second)
    print("Third: %s" % third)
    print("And all the rest... %s" % list(therest))


# Prints out
# First: 1
# Second: 2
# Third: 3
# And all the rest... [4, 5]
foo(1, 2, 3, 4, 5, 6)

"""
It is also possible to send functions arguments by keyword, 
so that the order of the argument does not matter, using the following syntax. 
The following code yields the following output: The sum is: 6 Result: 1


The "bar" function receives 3 arguments. 
If an additional "action" argument is received, and it instructs on summing up the numbers, 
then the sum is printed out. 
Alternatively, the function also knows it must return the first argument, if the value of the "number" parameter,
passed into the function, is equal to "first".
"""


def bar(first, second, third, **options):
    if options.get("action") == "sum":
        print("The sum is: %d" % (first + second + third))

    if options.get("number") == "first":
        return first


result = bar(1, 2, 3, action="sum", number="first")
print("Result: %d" % (result))

"""
Exercise
Fill in the foo and bar functions so they can receive a variable amount of arguments (3 or more) 
The foo function must return the amount of extra arguments received. 
The bar must return True if the argument with the keyword magicnumber is worth 7, and False otherwise.

# edit the functions prototype and implementation
def foo(a, b, c):
    pass

def bar(a, b, c):
    pass


# test code
if foo(1, 2, 3, 4) == 1:
    print("Good.")
if foo(1, 2, 3, 4, 5) == 2:
    print("Better.")
if bar(1, 2, 3, magicnumber=6) == False:
    print("Great.")
if bar(1, 2, 3, magicnumber=7) == True:
    print("Awesome!")
"""


# edit the functions prototype and implementation
def foo1(a, b, c, *args):
    return len(args)


def bar1(a, b, c, **kwargs):
    return kwargs["magicnumber"] == 7


# test code
if foo1(1, 2, 3, 4) == 1:
    print("Good.")
if foo1(1, 2, 3, 4, 5) == 2:
    print("Better.")
if bar1(1, 2, 3, magicnumber=6) == False:
    print("Great.")
if bar1(1, 2, 3, magicnumber=7) == True:
    print("Awesome!")
