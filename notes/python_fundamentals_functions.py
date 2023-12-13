# Functions
# A function is a named block of code that we can execute to perform a specific task.
# Syntax for functions is: def

def add(a,b):
    x = a + b
    return x

new_val = add(3, 5)
print(new_val)
# Output: 8


# Parameters and Arguments
# def print_name(parameter):
#     print(parameter)
# print_name(arguments)

def print_name(name):
    print(name)

print_name("Alice")
# Output: Alice


# Returning Values

def say_hi(name):
    return "Hi " + name
greeting = say_hi("Ben")
print(greeting)
# Output: Hi Ben
