# Instance attributes are defined in the constructor, the special '__init__' method, which is called when a new object is instantiated.
# The first parameter of an instance method within a class will be 'self', and the instance attributes are also indicated by 'self'.
# 'self' is reference to the instance, not the class.

# Passing in Arguments
class Shoe:
    # now our method has 4 parameters (including self)
    def __init__(self, brand, shoe_type, price):
        # we assign them accordingly
        self.brand = brand
        self.type = shoe_type
        self.price = price
        # the status is set to True by default
        self.in_stock = True
skater_shoe = Shoe("Vans", "Low-top Trainers", 59.99)
dress_shoe = Shoe("Jack & Jill Bootery", "Ballet Flats", 29.99)
print(skater_shoe.type)	# output: Low-top Trainers
print(dress_shoe.type)	# output: Ballet Flats

# Methods are functions that belong to a class, and it must be called from an instance of a class.