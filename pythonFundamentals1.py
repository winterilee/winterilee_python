# Code blocks
# For functions, use "def"
# For conditional statements, use "if", "elif", "else"
# For loops, use "for", "while"
# For classes, use "Class"


# Primitive data types
# *Numbers -> Integers(whole numbers), floating point numbers(decimal numbers), and complex numbers.
age = 28
weight = 130.28

# *Strings -> Text.
fruit = "Blueberry"

# *Boolean Values -> Assesses the truth value of something. It has only two values: True and False(Uppercase T and F).
is_hungry = False


# Composite types
# *Tuples -> A type of data that is "immutable" (can't be modified after its creation) and can hold a group of values. Tuples can contain mixed data types.
cat = ("Skippy", "Calico", 3, False)
print(cat[0])

# *Lists -> A type of data that is "mutable" and can hold a group of values. Usually meant to store a collection of related data.
vegetables = ["Celery", "Onion", "Cucumber"]
vegetables[1] = "Asparagus"
vegetables.append("Broccoli")
print(vegetables)
vegetables.pop()

# *Dictionaries -> A group of key-value pairs. Dictionary elements are indexed by unique keys which are used to access values.
rescue_dog = {"name": "Beau", "age": 1, "weight": 9.2, "vaccinated": False}
rescue_dog["vaccinated"] = True
print(rescue_dog)


# Common Functions
# Use "type" function to find out the data type for variables:
print(type(3.14))
print(type(rescue_dog))

# Use "len" function to get the length:
print(len(rescue_dog))
print(len("Tomato"))