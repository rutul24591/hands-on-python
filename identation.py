"""
Python provides no braces to indicate blocks of code for class and function definitions or flow control.

Blocks of code are denoted by line indentation, which is rigidly enforced.

The number of spaces in the indentation is variable, but all statements within the block must be indented the same amount.
"""


# This is correct
"""
    if True:
       print "True"
    else:
       print "False"
"""

# However this block will generate error

"""
if True:
print "Answer"
print "True"
else:
print "Answer"
print "False"
"""

x = 1

if x == 1:
    print('X is 1')
else:
    print('X is not 1')