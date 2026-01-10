# Strings are defined either with a single quote or a double quotes.
""" The difference between the two is that using double quotes makes it easy to include apostrophes
(whereas these would terminate the string if using single quotes) """
mystring = 'hello'
print("mystring 1:" + " " + mystring)
mystring = "hello"
print("mystring 2:" + " " + mystring)

mystring = "Don't worry about apostrophes"
print("mystring 3:" + " " + mystring)

# Simple operators can be executed on numbers and strings:
one = 1
two = 2

three = one + two
print(three)

hello = "hello"
world = "world"
helloworld = hello + " " + world
print(helloworld)

# Assignments can be done on more than one variable "simultaneously" on the same line like this
a, b = 1, 2
print(a, b)

# Mixing operators between numbers and strings is not supported:
# This will not work!
one = 1
two = 2
hello = "hello"

# print(one + two + hello)



# Exercise:

mystring = "hello"
myfloat2 = 10.0
myint2 = 20

# testing code
if mystring == "hello":
    print("String: %s" % mystring)
if isinstance(myfloat2, float) and myfloat2 == 10.0:
    print("Float: %f" % myfloat2)
if isinstance(myint2, int) and myint2 == 20:
    print("Integer: %d" % myint2)

