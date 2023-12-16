# Instance attributes are defined in the constructor, the special '__init__' method, which is called when a new object is instantiated.
# The first parameter of an instance method within a class will be 'self', and the instance attributes are also indicated by 'self'.
# 'self' is reference to the instance, not the class.

# Passing in arguments
class Shoe:
    # now our method has 4 parameters (including self)
    def __init__(self, brand, shoe_type, price):
        # we assign them accordingly
        self.brand = brand
        self.type = shoe_type
        self.price = price
        # the status is set to True by default
        self.in_stock = True
    
    # creating a method that takes a float/percent as an argument and reduces the price of the item by the percentage.
    def on_sale_by_percent(self, percent_off):
        self.price = self.price * (1-percent_off)

# Creating instances:
skater_shoe = Shoe("Vans", "Low-top Trainers", 59.99)
dress_shoe = Shoe("Jack & Jill Bootery", "Ballet Flats", 29.99)
print(skater_shoe.type)	# output: Low-top Trainers
print(dress_shoe.type)	# output: Ballet Flats

# Methods are functions that belong to a class, and it must be called from an instance of a class.
class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
    # adding a method:
    def greeting(self):
        print(f"Hello, my name is {self.name}")
# The first parameter of every method within a class should be 'self'.

# Changing the class, Shoe, without methods
# The skater shoes go on sale by 20% reduced price:
skater_shoe.price = skater_shoe.price * (1 - 0.2)
# The dress shoes go on sale by 10% reduction:
dress_shoe.price = dress_shoe.price * (1 - 0.1)
# The skater shoes go on sale AGAIN by another 10%:
skater_shoe.price = skater_shoe.price * (1 - 0.1)