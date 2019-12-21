# 9-4 Number Served start from exercise 9.1 and add an attribute called number_served with default value of 0.
# Add a method called set_number_served() to set number of customers served.
# Add a method called increment_number_served() to allow increment the number of customers served.
class Restaurant:
    """A restaurant model with name and cuisine_type."""
    def __init__(self, name, cuisine_type):
        """Initialize name and cuisine_type."""
        self.name = name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        """Prints two pieces of information of restaurant."""
        print(f"The name of the restaurant is {self.name.title()}, and they serve {self.cuisine_type} food.")

    def open_restaurant(self):
        """Print a message to indicate restaurant is open."""
        print(f"{self.name.title()} is open right now!")

    def set_number_served(self, number):
        """Allows to set the number of customers the restaurants has served."""
        self.number_served = number

    def increment_number_served(self, add_served):
        """Allows to add the number of customers the restaurants has served."""
        self.number_served += add_served


restaurant = Restaurant('the happy place', 'everything')
print(f"This restaurant has served {restaurant.number_served} people.")

restaurant.number_served = 10
print(f"This restaurant has served {restaurant.number_served} people.")

# Testing the call method to set the number of people served.
restaurant.set_number_served(50)
print(f"This restaurant has served {restaurant.number_served} people.")

# Call method to increment number of people served.
restaurant.increment_number_served(25)
print(f"This restaurant has served {restaurant.number_served} people.")





# 9-5 Login Attempts: From exercise 9.3, add an attribute called login_attempts.
# Write a method called increment_login_attempts() that increments by 1.
# Write another method called reset_login_attempts() that resets the value of login_attempts to 0.
# Make an instance of the User class and call increment_login_attempts() several times.
# Print the value to make sure it was incremented properly, and then reset using reset_login_attempts().
# Verify the values by printing it.
class User:
    
    """Create several other usernames and attributes typically stored in a user profile."""
    def __init__(self, first_name, last_name, username, age, location):
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.username = username
        self.age = age
        self.location = location.title()
        self.login_attempts = 0


    """Create a method describe_user() to print a summary of user's information."""
    def describe_user(self):
        print(f"\nHere is a summary of the user's profile for {self.username}:")
        print(f"\tName: {self.first_name} {self.last_name}")
        print(f"\tAge: {self.age}")
        print(f"\tLocation: {self.location}")

    """Greet the user with a personalized message called method greet_user()."""
    def greet_user(self):
        print(f"Hello, {self.username}! I hope you are doing well today!")

    """Increment user login attempts by 1."""
    def increment_login_attempts(self):
        self.login_attempts += 1

    """Reset login attempts to 0."""
    def reset_login_attempts(self):
        self.login_attempts = 0


tyson = User('tyson', 'nguyen', 'tyson.nguyen', '22', 'united states')
tyson.describe_user()
tyson.greet_user()

tyson.increment_login_attempts()
tyson.increment_login_attempts()
tyson.increment_login_attempts()
print(tyson.login_attempts)

tyson.reset_login_attempts()
print(f"The login is now reset back to {tyson.login_attempts}.")