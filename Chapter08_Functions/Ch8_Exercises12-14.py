# 8-12 Sandwiches: Write a function that accepts a list of items a person wants on a sandwich with one parameter.
def make_sandwich(*ingredients):
    """Collect as many ingredients what a person wants on a sandwich and make it."""
    print("\nI am going to make a sandwich for you. Please list all the ingredients you would like on your sandwich:")
    for ingredient in ingredients:
        print(f"- {ingredient}")

make_sandwich('cheese', 'peppers', 'pepperoni', 'ham')
make_sandwich('metal', 'plastic', 'dirt', 'rocks', 'dust particles')
make_sandwich('bread', 'ketchup')


# 8-13 User Profile: Start with a copy of user_profile. Build a profile of yourself by calling build_profile().
def build_profile(first, last, **user_info):
    """Building a dictionary containing information about the user."""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

user_profile = build_profile('tyson', 'nguyen', location='oregon', interest='technology', personality='chill')
print(user_profile)


# 8-14 Cars: Write a function that stores information about a car in a dictionary.
# The function should always have a manufacturer and a model name. Then accept an arbitrary number of keyword arguments.
def make_car(manufacturer, model, **car_info):
    """Build a car dictionary for all the information about a vehicle."""
    car_info['manufacturer'] = manufacturer
    car_info['model'] = model
    return car_info

car = make_car('tesla', 'model 3', color='blue', price='$40000', range='250 miles')
print(car)