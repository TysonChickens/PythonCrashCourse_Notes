"""A set of privileges for admin user."""

from only_user import User

class Admin(User):
    """Class that inherits from User."""

    def __init__(self, first_name, last_name, username, age, location):
        """Initialize the admin user and admin privileges attribute."""
        super().__init__(first_name, last_name, username, age, location)
        self.privileges = Privileges()

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