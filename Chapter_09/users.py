"""A set of classes for user privileges for admin user."""

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
