# 9-1: Create three different instances from the class Restaurant and describe each.
class Restaurant:
    """A restaurant model with name and cuisine_type."""
    def __init__(self, name, cuisine_type):
        """Initialize name and cuisine_type."""
        self.name = name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """Prints two pieces of information of restaurant."""
        print(f"The name of the restaurant is {self.name.title()}, and they serve {self.cuisine_type} food.")

    def open_restaurant(self):
        """Print a message to indicate restaurant is open."""
        print(f"{self.name.title()} is open right now!")

restaurant = Restaurant('the happy place', 'everything')

print(f"{restaurant.name}, {restaurant.cuisine_type}.")
restaurant.describe_restaurant()
restaurant.open_restaurant()


# 9-2: Create three different instances from the class of Restaurant, and call describe_restaurant() for each instance.
bad_restaurant = Restaurant('the bad place', 'nothing')
bad_restaurant.describe_restaurant()

pizza_place = Restaurant('overpizza', 'pizza')
pizza_place.describe_restaurant()

sweet = Restaurant('you sweet', 'candy')
sweet.describe_restaurant()


# 9-3: Make a class called User and create two attributes called first_name and last_name.
class User:
    
    """Create several other usernames and attributes typically stored in a user profile."""
    def __init__(self, first_name, last_name, username, age, location):
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.username = username
        self.age = age
        self.location = location.title()


    """Create a method describe_user() to print a summary of user's information."""
    def describe_user(self):
        print(f"\nHere is a summary of the user's profile for {self.username}:")
        print(f"\tName: {self.first_name} {self.last_name}")
        print(f"\tAge: {self.age}")
        print(f"\tLocation: {self.location}")

    """Greet the user with a personalized message called method greet_user()."""
    def greet_user(self):
        print(f"Hello, {self.username}! I hope you are doing well today!")


# Creating different instances of users.
cookies = User('chocolate', 'cookies', 'chip', 'unknown', 'united states')
cookies.describe_user()
cookies.greet_user()

tyson = User('tyson', 'nguyen', 'tyson.nguyen', '22', 'united states')
tyson.describe_user()
tyson.greet_user()


