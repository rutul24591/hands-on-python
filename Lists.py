myList = []

myList.append(1)
myList.append(2)
myList.append(3)

print("My list: ", myList)
print("Length of List: ", len(myList))

# Note: index is 0-based
print(myList[0])    # prints 1
print(myList[1])    # prints 2
print(myList[2])    # prints 3

# Prints out 1,2,3
print("* My List *")
for item in myList:
    print(item)

# Accessing an index which does not exist generates an exception (an error).
mylist = [1,2,3]
# print(mylist[10])



# Exercise

numbers = []
strings = []
names = ["John", "Eric", "Jessica"]

numbers.append(1)
numbers.append(2)
numbers.append(3)

strings.append("hello")
strings.append("world")

# write your code here
second_name = strings[1]


# this code should write out the filled arrays and the second name in the names list (Eric).
print(numbers)
print(strings)
print("The second name on the names list is %s" % second_name)