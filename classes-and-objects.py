"""
Classes and Objects
Objects are an encapsulation of variables and functions into a single entity.
Objects get their variables and functions from classes.
Classes are essentially a template to create your objects.

A very basic class would look something like this:

class MyClass:
    variable = "blah"

    def function(self):
        print("This is a message inside the class.")
"""


# How to assign to an object.
class MyClass:
    variable = "blah"

    def function(self):
        print("This is a message inside the class.")


myobjectx = MyClass()

# Now the variable "myobjectx" holds an object of the class "MyClass"
# that contains the variable and the function defined within the class called "MyClass".


"""
Accessing Object Variables
To access the variable inside of the newly created object "myobjectx" you would do the following:

myobjectx.variable
"""
print(myobjectx.variable)

"""
You can create multiple different objects that are of the same class(have the same variables and functions defined).
However, each object contains independent copies of the variables defined in the class. 
For instance, if we were to define another object with the "MyClass" class and then change the string in the variable above:
"""


class MyClass:
    variable = "blah"

    def function(self):
        print("This is a message inside the class.")


myobjectx = MyClass()
myobjecty = MyClass()

myobjecty.variable = "yackity"

# Then print out both values
print(myobjectx.variable)
print(myobjecty.variable)

"""
Accessing Object Functions
To access a function inside of an object you use notation similar to accessing a variable:
"""
myobjectx.function()

"""
init()
The __init__() function, is a special function that is called when the class is being initiated. It's used for assigning values in a class.
"""


class NumberHolder:

    def __init__(self, number):
        self.number = number

    def returnNumber(self):
        return self.number


var = NumberHolder(7)
print(var.returnNumber())  # Prints '7'

"""
Exercise


"""


# define the Vehicle class
class Vehicle:
    name = ""
    kind = "car"
    color = ""
    value = 100.00

    # one way
    def __init__(self, name, color, kind, value):
        self.name = name
        self.color = color
        self.kind = kind
        self.value = value

    def description(self):
        desc_str = "%s is a %s %s worth $%.2f." % (
            self.name,
            self.color,
            self.kind,
            self.value,
        )
        return desc_str


# your code goes here
car1 = Vehicle("Fer", "red", "convertible", 60000.00)
car2 = Vehicle("Jump", "blue", "van", 10000.00)

# second way
# Remove __init__ from Class above
# car1 = Vehicle()

# car1.name = "Fer"
# car1.color = "red"
# car1.kind = "convertible"
# car1.value = 60000.00

# car2 = Vehicle()

# car2.name = "Jump"
# car2.color = "blue"
# car2.kind = "van"
# car2.value = 10000.00


# test code
print(car1.description())
print(car2.description())
