# Dictionaries
# A dictionary is another mutable sequence type that can store any number of Python objects.
# Dictionaries consist of pairs(called items) of keys and their corresponding values.

person = {"first": "Ada", "last": "Lovelace", "age": 42, "is_organ_donor": True}
capitals = {}


# Adding New Key-Value Pairs
capitals["svk"] = "Bratislava"
capitals["deu"] = "Berlin"
capitals["dnk"] = "Copenhagen"


# List Syntax:
# my_list[0] = 2
# Dictionary Syntax:
# my_dict["some_string"] = some_value


# Changing or Updating Values
person["email"] = "alovelace@codingdojo.com"
person["last"] = "Bobada"
print(person)


# Testing for an Existing Key
# if some_key in my_dictionary:
#   update the value

if "email" not in person:
    person["email"] = "newemail@email.com"
else:
    print("Would you like to replace your existing email?")


# Accessing Values
print(person["first"])
full_name = person["first"] + " " + person["last"]
print(full_name)


# Removing Values
# There are 2 ways to remove a key:value pair from a dictionary:
value_removed = capitals.pop('svk')
del capitals['dnk']


# Multi-Line Syntax
person2 = {
    "first": "Ben",
    "last": "Stuart",
    "age": 39,
    "is_organ_donor": False
}


# Common Built-In Functions and Methods:
# len() -> give the total length of the dictionary.
# str() -> produces a string representation of a dictionary.
# type() -> returns the type of the passed variable. If passed variable is a dictionary, it will then return a 'dict' type.

# Some of useful Python dictionary methods:
# .clear() -> removes all elements from the dictionary
# .get(key, default=None) -> A safe way to get a value, if the key might not exist. Return the value for the specified key or 'None' (or a value you specify) if the key is not in the dictionary.
# .update(pairs_to_update) -> Add and update multiple key-value pairs at once, by passing in another dictionary of the pairs to update and add.


# For Loops through Dictionaries
my_dict = {"name": "Noelle", "language": "Python"}
for each_key in my_dict:
    print(each_key)
# Output: name, language

for each_key in my_dict:
    print(my_dict[each_key])
# Output: Noelle, Python

us_capitals = {
    "Washington":"Olympia",
    "California":"Sacramento",
    "Idaho":"Boise",
    "Illinois":"Springfield",
    "Texas":"Austin",
    "Oklahoma":"Oklahoma City",
    "Virginia":"Richmond"}

for key in us_capitals.keys():
    print(key)
# Output: Washington, California, Idaho, Illinois, Texas, Oklahoma, Virginia

for val in us_capitals.values():
    print(val)
# Output: Olympia, Sacramento, Boise, Springfield, Austin, Oklahoma City, Richmond

for key, val in us_capitals.items():
    print(key, " = ", val)
# Output: Washington = Olympia, California = Sacramento, Idaho = Boise, etc


# Nesting
# List of dictionaries
users = [
    {"first": "Ada", "last": "Lovelace"}, # index 0
    {"first": "Alan", "last": "Turing"}, # index 1
    {"first": "Eric", "last": "Idle"} # index 2
]
# Dictionary of lists
resume_data = {
    #        	     0           1           2
    "skills": ["front-end", "back-end", "database"],
    #                0           1
    "languages": ["Python", "JavaScript"],
    #                0              1
    "hobbies":["rock climbing", "knitting"]
}


# Accessing Values in Nested Dictionaries
print(users[0]["last"]) # prints Lovelace