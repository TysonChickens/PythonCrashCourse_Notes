"""A restaurant class to model real-world."""

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