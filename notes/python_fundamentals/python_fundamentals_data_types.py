# Numbers
# *int -> whole numbers, positive or negative.
# *float -> decimal numbers, positive or negative.
# *complex -> are a part of the real number system and are often referenced with the letter "j".

# Type
print(type(99))
print(type(7.72))
print(type(2j))

# Conversion
int_to_float = float(22)
float_to_int = int(9.18)
int_to_complex = complex(88)

# Random Number
# Python doesn't have a built in random, so it needs to be imported.
import random
# Provide a random number between 1 and 9:
print(random.randint(1,9))


# Strings
# Strings are any sequence of characters enclosed in single or double quotes.
print("This is a string")

# Concatenating Strings and Variables with the print function
breakfast = "Blueberry muffins"
print("Today's breakfast is ", breakfast)
print("Today's breakfast is " + breakfast)

# Type Casting or Explicit Type Conversion
# *integer to string
# The following will not work:
# print("The temperature is " + 77)
# The following will work:
print("The temperature is " + str(77))

# *string to integer
value1 = 22
value2 = "44"
# The following will not work:
# total1 = value1 + value2
# The following will work:
total2 = value1 + int(value2)

# String Interpolation
# We can inject variables into our strings, which is known as "string interpolation".
menu = "pumpkin soup"
amount1 = 1
amount2 = 2
measurement1 = "tsp"
measurement2 = "tbsp"
# *F-String
print(f"The {menu} needs {amount1} {measurement1} of salt and {amount2} {measurement2} of sugar.")

# *string.format()
print("The {} needs {} {} of salt and {} {} of sugar.".format(menu, amount1, measurement1, amount2, measurement2))

# *%-formatting
# "%s" for a string and "%d" for a number.
print("The %s needs %s %s of salt and %s %s of sugar." % (menu, amount1, measurement1, amount2, measurement2))

# Built-In String Methods
# * string.title(): returns a copy of the string with all the first character of words in uppercase.
# * string.upper(): returns a copy of the string with all the characters in uppercase.
# * string.lower(): returns a copy of the string with all the characters in lowercase.
# * string.count(substring): returns number of occurrences of substring in string.
# * string.split(char): returns a list of values where string is split at the given character. Without a parameter the default split is at every space.
# * string.find(substring): returns the index of the start of the first occurrence of substring within string.
# * string.isalnum(): returns boolean depending on whether the string's length is > 0 and all characters are alphanumeric (letters and numbers only). Strings that include spaces and punctuation will retun False for this method. Similar methods include ".isalpha()", ".isdigit()", ".islower()", ".isupper()", and so on. All return booleans.
# * string.join(list): returns a string that is all strings within our set (in this case a list) concatenated.
# * string.endswith(substring): returns a boolean based upon whether the last characters of string match substring.