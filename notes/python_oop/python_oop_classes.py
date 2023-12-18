# OOP (Object Oriented Programming)

# Classes are blueprints of objects.
# The basic building blocks of objects are 'attributes' and 'methods'.
# Attributes are characteristics shared by all instances of the class type.
# Methods are actions that an object can perform.

# A constructor is a function that contains instructions for making a new instance of a class.
# In Python, this is a special function called the '__init__' method.

# Class example:
class Shoe:
    # constructor:
    def __init__(self):
        # attributes:
        self.brand = "Adidas"
        self.type = "tenis shoe"
        self.price = 45.99
        self.in_stock = True
    
    # methods:
    def rebrand(self, new_brand):
        self.brand = new_brand
    
    def sold_out(self):
        self.in_stock = False
    
    def on_sale(self, percent):
        self.price = self.price*(1-percent)

# Making Instances:
new_shoe = Shoe()