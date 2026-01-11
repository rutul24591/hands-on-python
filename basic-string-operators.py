# Strings are bits of text. They can be defined as anything between quotes:
astring = "Hello world!"
astring2 = "Hello world!"

"""
As you can see, the first thing you learned was printing a simple sentence. 
This sentence was stored by Python as a string. 
However, instead of immediately printing strings out, we will explore the various things you can do to them. 
You can also use single quotes to assign a string. 
However, you will face problems if the value to be assigned itself contains single quotes. 
For example to assign the string in these bracket(single quotes are ' ') you need to use double quotes only like this
"""

print("single quotes are ' '")

print(len(astring))  # 12
print(
    astring.index("o")
)  # 4  That prints out 4, because the location of the first occurrence of the letter "o" is 4 characters away from the first character.
print(astring.count("l"))  # 3

"""
-   This prints a slice of the string, starting at index 3, and ending at index 6. But why 6 and not 7.
-   If you just have one number in the brackets, it will give you the single character at that index. 
-   If you leave out the first number but keep the colon, it will give you a slice from the start to the number you left in.
-   If you leave out the second number, it will give you a slice from the first number to the end.
-   You can even put negative numbers inside the brackets. 
    They are an easy way of starting at the end of the string instead of the beginning. 
    This way, -3 means "3rd character from the end".
"""
print(astring[3:7])  # lo w     3 inclusive and 7 exclusive(till position 6)
print(astring[2])  # l
print(astring[2:])  # llo world!
print(astring[:4])  # Hell
print(astring[-4])  # r.    End index begins with -1

# This prints the characters of string from 3 to 7 skipping one character.
# This is extended slice syntax. The general form is [start:stop:step].
print(astring[3:7:2])  # l  ???? Doubt over here

# There is no direct function to reverse a string in python, but it can be easily done using
print(astring[::-1])  # !dlrow olleH

# Convert to uppercase or turn to lowercase
print(astring.upper())
print(astring.lower())

# This is used to determine whether the string starts with something or ends with something, respectively.
print(astring.startswith("Hello"))
print(astring.endswith("asdfasdfasdf"))  # As no match. String not ending with asdfa...

# Split the string by " " and return it in array
afewwords = astring.split(" ")
print("Splitted string: ", afewwords)  # ['Hello', 'world!']

"""
Exercise

Try to fix the code to print out the correct information by changing the string.

s = "Hey there! what should this string be?"
# Length should be 20
print("Length of s = %d" % len(s))

# First occurrence of "a" should be at index 8
print("The first occurrence of the letter a = %d" % s.index("a"))

# Number of a's should be 2
print("a occurs %d times" % s.count("a"))

# Slicing the string into bits
print("The first five characters are '%s'" % s[:5]) # Start to 5
print("The next five characters are '%s'" % s[5:10]) # 5 to 10
print("The thirteenth character is '%s'" % s[12]) # Just number 12
print("The characters with odd index are '%s'" %s[1::2]) #(0-based indexing)
print("The last five characters are '%s'" % s[-5:]) # 5th-from-last to end

# Convert everything to uppercase
print("String in uppercase: %s" % s.upper())

# Convert everything to lowercase
print("String in lowercase: %s" % s.lower())

# Check how a string starts
if s.startswith("Str"):
    print("String starts with 'Str'. Good!")

# Check how a string ends
if s.endswith("ome!"):
    print("String ends with 'ome!'. Good!")

# Split the string into three separate strings,
# each containing only a word
print("Split the words of the string: %s" % s.split(" "))
"""

s = "Strings are awesome!"
# Length should be 20
print("Length of s = %d" % len(s))

# First occurrence of "a" should be at index 8
print("The first occurrence of the letter a = %d" % s.index("a"))

# Number of a's should be 2
print("a occurs %d times" % s.count("a"))

# Slicing the string into bits
print("The first five characters are '%s'" % s[:5])  # Start to 5   Strin
print("The next five characters are '%s'" % s[5:10])  # 5 to 10     gs ar
print("The thirteenth character is '%s'" % s[12])  # Just number 12   a
print(
    "The characters with odd index are '%s'" % s[1::2]
)  # (0-based indexing)   tig r wsm!
print("The last five characters are '%s'" % s[-5:])  # 5th-from-last to end     some!

# Convert everything to uppercase
print("String in uppercase: %s" % s.upper())  # STRINGS ARE AWESOME!

# Convert everything to lowercase
print("String in lowercase: %s" % s.lower())  # strings are awesome!

# Check how a string starts
if s.startswith("Str"):
    print("String starts with 'Str'. Good!")

# Check how a string ends
if s.endswith("ome!"):
    print("String ends with 'ome!'. Good!")

# Split the string into three separate strings,
# each containing only a word
print(
    "Split the words of the string: %s" % s.split(" ")
)  # ['Strings', 'are', 'awesome!']
