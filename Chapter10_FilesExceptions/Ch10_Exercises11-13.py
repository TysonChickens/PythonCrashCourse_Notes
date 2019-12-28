# 10-11 Favorite number
import json

filename = 'Chapter10_FilesExceptions/favorite_number.json'
favorite_number = input("What is your favorite number? ")
with open(filename, 'w') as f:
    json.dump(favorite_number, f)

with open(filename) as f:
    favorite = json.load(f)
    print(f"I know your favorite number is {favorite}!")


# 10-12 Remember favorite number
import json

filename = 'Chapter10_FilesExceptions/favorite_number.json'
try:
    with open(filename) as f:
        favorite = json.load(f)
except FileNotFoundError:
    favorite_number = input("What is your favorite number? ")
    print("I will remember it when you come back.")
    with open(filename, 'w') as f:
        json.dump(favorite_number, f)
else:
    print(f"Your favorite number is {favorite}!")



# 10-13 Verify User
import json

def get_stored_username():
    """Get stored username if available."""
    filename = 'Chapter10_FilesExceptions/username.json'
    try:
        with open(filename) as f:
            username = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return username

def get_new_username():
    """Prompt for a new username."""
    username = input("What is your name? ")
    filename = 'Chapter10_FilesExceptions/username.json'
    with open(filename, 'w') as f:
        json.dump(username, f)
        return username

def greet_user():
    """Greet the user by name."""
    username = get_stored_username()
    if username:
        print(f"Welcome back, {username}!")
        confirm_username = input("Is this your username? Yes/No: ").lower()
        if confirm_username == "yes":
            print(f"Welcome back, {username}!")
        else:
            username = get_new_username()
            print(f"We'll remember you when you come back, {username}!")
    else:
        username = get_new_username()
        print(f"We'll remember you when you come back, {username}!")

greet_user()

