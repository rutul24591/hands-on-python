# Python uses C-style string formatting to create new, formatted strings.
# The "%" operator is used to format a set of variables enclosed in a "tuple" (a fixed size list),
# together with a format string, which contains normal text together with "argument specifiers",
# special symbols like "%s" and "%d".

name = "John"
print("Hello, %s!" % name)
# print("Hello, " + name + "!")     This also works

# To use two or more argument specifiers, use a tuple (parentheses):
age = 24

print("%s is %d years old." % (name, age))

"""
 Here are some basic argument specifiers you should know:

 %s - String (or any object with a string representation, like numbers)

 %d - Integers

 %f - Floating point numbers

 %.<number of digits>f - Floating point numbers with a fixed amount of digits to the right of the dot.
 print("%.5f" % age)

 %x/%X - Integers in hex representation (lowercase/uppercase)
 print("%x" % age)
"""

""" 
Exercise

You will need to write a format string which prints out the data using the following syntax: Hello John Doe. 
Your current balance is $53.44.

data = ("John", "Doe", 53.44)
format_string = "Hello"

print(format_string % data)
"""

data = ("John", "Doe", 53.44)
format_string = "Hello %s %s. Your current balance is $%s."

print(format_string % data)
