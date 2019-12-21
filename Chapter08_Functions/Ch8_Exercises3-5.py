# 8-3 T-Shirt: Write a function called make_shirt() that accepts a size and text that should be printed on the shirt.
def make_shirt(size, message):
    """Print a sentence summarizing the size of the shirt and the message printed on it."""
    print(f"The shirt should be printed in size {size} with a message of: {message}")

# Call the function with positional arguments.
make_shirt('small', 'This is fun!')

# Call the function with keyword arguments.
make_shirt(message='I am a keyword argument.', size='small')


# 8-4 Large Shirts: Modify make_shirt() so large shirts are default with message 'I love Python.'
def make_shirt1(size='large', message='I love Python.'):
    """Modify a large and medium shirt to default to message, and any other size with a different message."""
    print(f"The shirt size is a {size} with a message of: {message}")

make_shirt1()
make_shirt1('medium')
make_shirt1('small', 'I love life!')


# 8-5 Cities: Write a function called describe_city() that accepts name of city and country.
def describe_city(city, country='South Africa'):
    """Print a simple sentence where the city is located in a country."""
    print(f"{city.title()} is located in the country of {country.title()}.")

describe_city('Johannesburg')
describe_city('Cape Town')
describe_city(city='Portland', country='United States')