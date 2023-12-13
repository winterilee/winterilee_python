# Conditionals
# Conditional statements allow us to run certain lines of code depending on whether certain conditions are met.
# Python uses "if", "elif", and "else".
grade = 82
if grade >= 90:
    print("A")
elif grade >= 80:
    print("B")
elif grade >= 70:
    print("C")
elif grade >= 60:
    print("D")
else:
    print("F")

#Operators for conditionals:
# * == : Checks if the value of two operands are equal.
# * != : Checks if the value of two operands are not equal.
# * >  : Checks if the value of left operand is greater than the value of right operand.
# * <  : Checks if the value of left operand is less than the value of right operand.
# * >= : Checks if the value of left operand is greater than or equal to the value of right operand.
# * <= : Checks if the value of left operand is less than or equal to the value of right operand.
# * and: Checks that each expression on the left and right are both True.
# * or : Checks if either the expression on the left or right is True.
# * not: Reverses the true-false value of the operand.


# Loops
# For Loops with range()

# range(stop)
for i in range(5):
    print(i)
# Output: 0, 1, 2, 3, 4

# range(start, stop)
for i in range(2,7):
    print(i)
# Output: 2, 3, 4, 5, 6

# range(start, stop, step)
for i in range(2, 16, 3):
    print(i)
# Output: 2, 5, 8, 11, 14

# For Loops through Strings
for x in 'Hello':
    print(x)
# Output: 'H', 'e', 'l', 'l', 'o'

# For Loops through Lists
a_list = ["Hello", 456, "Goodbye"]
for i in range(0, len(a_list)):
    print(i, a_list[i])
# Output: 0 Hello, 1 456, 2 Goodbye

for v in a_list:
    print(v)
# Output: Hello, 456, Goodbye


# While Loops
count = 0
while count <= 5:
    print("looping - ", count)
    count +=1
# Output: looping - 0, looping - 1, looping - 2, looping - 3, looping - 4, looping - 5

x = 0
y = 3
while x <= y:
    print(x)
    x = x + 1
else:
    print("The end of the while loop")
# Output: 0, 1, 2, 3, The end of the while loop


# Loop Control

for val in "string":
    if val == "i":
        break
    print(val)
# Output: s, t, r

for val in "string":
    if val == "i":
        continue
    print(val)
# Output: s, t, r, n, g
