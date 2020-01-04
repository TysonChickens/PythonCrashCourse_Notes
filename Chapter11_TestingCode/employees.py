class Employee:
    """Information about an employee."""
    
    def __init__(self, first, last, salary):
        """Initialize attributes for employee."""
        self.first = first.title()
        self.last  = last.title()
        self.salary = salary

    def give_raise(self, amount=5000):
        """Add $5,000 to the annual salary by default but also accept a different amount."""
        self.salary += amount
