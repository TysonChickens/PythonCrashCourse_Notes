# 9-6 Ice Cream Stand: An ice cream stand is a specific kind of restaurant.
# Write a class called IceCreamStand inherited from Restaurant class from Exercise 9.1 or 9.4

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

class IceCreamStand(Restaurant):
    """Ice cream stand from parent class of Restaurant."""

    def __init__(self, name, cuisine_type='ice_cream'):
        """Initialize attributes of the parent class."""
        super().__init__(name, cuisine_type)
        self.flavors = []

    def show_flavors(self):
        """Print a statement showing the flavors."""
        print(f"Here are the ice cream flavors offered here:")
        for flavor in self.flavors:
            print(f"- {flavor.title()}.")

icecream = IceCreamStand('frozen land')
icecream.flavors = ['vanilla', 'chocolate', 'peanut butter']

icecream.show_flavors()



# 9-7 Admin: Write a class called Admin that inherits from the User class in Exercise 9.3 or Exercise 9.5
# Add an attribute privileges that stores a list of strings like "can add post", "can delete post", "can ban user"...
# Write a method called show_privileges() that lists admin privileges.

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


# 9-7 Admin user privileges inherit from User class.

class Admin(User):
    """Class that inherits from User."""

    def __init__(self, first_name, last_name, username, age, location):
        """Initialize the admin user and admin privileges attribute."""
        super().__init__(first_name, last_name, username, age, location)
        self.privileges = Privileges()


    # """Method called show_privileges() that lists the admin's set of privileges."""
    # def show_privileges(self):
    #     print("\nPrivileges:")
    #     for privilege in self.privileges:
    #         print(f"- {privilege}")


# 9-8 Privileges Class Separate Instance as Attribute for Admin user.

class Privileges:
    """List of privileges only for the admin user."""

    def __init__(self, privileges=[]):
        """Initialize only one attribute for privileges."""
        self.privileges = privileges

    """Method called show_privileges() that lists the admin's set of privileges."""
    def show_privileges(self):
        print("\nPrivileges:")
        if self.privileges:
            for privilege in self.privileges:
                print(f"- {privilege}")
        else:
            print("This user has no privileges.")

tyson = Admin('tyson', 'nguyen', 'tysonnguyen', 22, 'oregon')
tyson.describe_user()

tyson.privileges.show_privileges()

print("\nAdding privileges for Tyson:")
tyson.privileges.privileges = ['ban people', 'reset password', 'edit posts']
tyson.privileges.show_privileges()


# 9-9 Battery Upgrade to electric car with upgrade_battery() method.

class Car:

    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Return a formatted descriptive name."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def update_odometer(self, mileage):
        """Set the odometer reading to the given value.
        Reject the change if it attempts to roll the odometer back.
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        """Add the given amount to the odometer reading."""
        self.odometer_reading += miles

    def read_odometer(self):
        """Print a statement showing the car's mileage."""
        print(f"This car has {self.odometer_reading} miles on it.")

class Battery:
    """A simple attempt to model a battery for an electric car."""

    def __init__(self, battery_size=75):
        """Initialize battery attributes."""
        self.battery_size = battery_size

    def describe_battery(self):
        """Print a statement describing the battery size."""
        print(f"This car has a {self.battery_size}-kWh battery.")

    def get_range(self):
        """Print a statement about the range this battery provides."""
        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 100:
            range = 315
        print(f"This car can go about {range} miles on a full charge.")

    # 9-9 battery_upgrade method to check battery size and capacity.

    def upgrade_battery(self):
        if self.battery_size != 100:
            print("\nWe upgraded the battery size to 100.")
            self.battery_size = 100

class ElectricCar(Car):
    """Represents aspects of a car, specific to electric vehicles."""
    
    def __init__(self, make, model, year):
        """Initialize attributes of the parent class."""
        super().__init__(make, model, year)
        self.battery_size = 75
        self.battery = Battery()

    def describe_battery(self):
        """Print a statement describing the battery size."""
        print(f"This car has a {self.battery_size}-kWh battery.")


my_tesla = ElectricCar('tesla', 'model s', 2019)
upgraded_tesla = ElectricCar('tesla', 'model 3', 2019)

upgraded_tesla.battery.get_range()

upgraded_tesla.battery.upgrade_battery()
upgraded_tesla.battery.get_range()

