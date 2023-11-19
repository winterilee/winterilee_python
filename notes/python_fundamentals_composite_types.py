# Tuples "()"
# Tuple is a container for a fixed sequence of data objects. Tuples are immutable and use parentheses.
fruits = ("blueberry", "strawberry", "banana", "grapefruit")


# Lists "[]"
# List is also known as an "array" in other programming languages. This data type allows you to hold groups of values.
# Lists are created with values inside of square brackets, "[]", where each value is separated by a comma. They can be updated by adding values and/or by deleting values.
primary_colors = ["red", "yellow", "blue"]

# In Python, you can combine them and duplicate values by using "+" and "*" operators.
# If you "add" lists together, it will create a new list that contains all the values of both of the lists.
# If you "multiply" a list by a whole number it will copy all of the values that many times, and make a new list with all the copied values.
ingredient1 = ["strawberry", "banana"]
ingredient2 = ["apple juice"]
strawberry_shake = ingredient1 + ingredient2
print(strawberry_shake)
order1 = strawberry_shake * 2
print(order1)

# Appending Values to a List
index_list = [0,1,2,3]
index_list.append(4)
print(index_list)

# Slicing
# Using the syntax: "[:]", it will return a copy of some portion of the list, constrained by specified indices.
index_string = ["zero", "one", "two", "three", "four"]
print(index_string[1:])
print(index_string[:4])
print(index_string[2:4])

# Built-in Functions for Sequences
# * len(sequence): returns the length (number of items) in a sequence.
# * max(sequence): returns the highest value in a sequence.
# * min(sequence): returns the lowest value in a sequence.
# * sorted(sequence): returns a sorted sequence.

# Built-in List Methods
# * list.append(value): appends a value to the end of the list.
# * list.pop(index): remove a value at given position. If no parameter is passed, it will remove the last value in the list.
# * list.index(value): returns the index (position) of the given value if it exists in the list and raises an error if it does not exist.
# * list.reverse(): reverses the order of the elements, in place.
# * list.sort(): sorts the items in order of least to greatest, or alphabetically for strings, in place.


# Dictionaries "{}"
# Dictionary is another mutable sequence type that can store any number of Python objects. Dictionaries consist of pairs (called items) of keys and their corresponding values.
# Characteristics of Dictionaries:
# - A dictionary is an unordered collection of objects.
# - Values are accessed using a key (typically a string).
# - A dictionary caan shrink or grow as needed.
# - The contents of dictionaries can be modified.
# - Dictionaries can be nested.
# - Sequence operations such as slice cannot be used with dictionaries.
potluck = {"Joy": "Blueberry muffin", "Steve": "Pecan Pie"}
potluck["James"] = "Key Lime Pie"
potluck["Stacy"] = "Cornbread"
print(potluck)
# Dictionaries do not use index numbers.