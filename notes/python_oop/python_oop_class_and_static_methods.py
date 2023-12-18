# Instance methods: a normal methods such as when we declare and set attributes that don't belong to a single instance, but to the class itself. Likewise, when we create a method on a class we pass in 'self' to refer to the instance of hte object.

# Class attributes are defined outside of any instance methods, and are shared among all instances of the class.

# Class methods are defined with a decorator, '@classmethod'. They belong to the class itself instead of the instance. Instead of implicitly passing 'self' into the method, we pass 'cls'.
# Class methods have no access to the instance attribute or any attribute that starts with 'self'.

# Static methods are functions defined within the class with a decorator, '@staticmethod'. They have no access on instance or class attributes, so if we need any existing values, they need to be passed in as arguments.
# Static methods offer us the opportunity to organize in a better way.

class BankAccount:
    # class attributes
    bank_name = "First National Dojo"
    # new class attribute - a list of all the accounts
    all_accounts = []
    
    def __init__(self, int_rate, balance):
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.all_accounts.append(self)
    
    # class method to change the name of the bank
    @classmethod
    def change_bank_name(cls,name):
        cls.bank_name = name
    # class method to get balance of all accounts
    @classmethod
    def all_balances(cls):
        sum = 0
        # we use cls to refer to the class
        for account in cls.all_accounts:
            sum += account.balance
        return sum
    def with_draw(self,amount):
        # we can use the static method here to evaluate if we can withdraw the funds without going negative
        if BankAccount.can_withdraw(self.balance,amount):
            self.balance -= amount
        else:
            print("Insufficient Funds")
        return self
    
    # static methods have no access to any attribute, but only to what is passed into it
    @staticmethod
    def can_withdraw(balance,amount):
        if (balance - amount) < 0:
                return False
        else:
            return True

# Association between classes

class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(int_rate=0.02, balance=0)
    
    def example_method(self):
        # we can call the BankAccount instance's methods
        self.account.deposit(100)
        # or access its attributes
        print(self.account.balance)