# 5-8 Hello Admin: Make a list of five or more usernames, including the name 'admin'.
# Print a greeting to each user after they log in to a website. Loop through the list, and print greeting to each user.
usernames = ['admin', 'tyson', 'alex', 'president', 'kyle', 'samsung']

for username in usernames:
    if username == 'admin':
        print("Hello admin, would you like to see a status report?")
    else:
        print(f"Hello {username}, thank you for logging again!")

# 5-9 No Users: Add an if test to make sure list of users is not empty. 

empty_usernames = []
if empty_usernames:
    for username in empty_usernames:
        print(f"Here is the list of usernames {username}.")
else:
    print("There are no usernames. We need to find some users!")

# 5-10 Checking Usernames: Create a program that simulates websites ensure that everyone has a unique name.
current_users = ['apple', 'google', 'samsung', 'pc', 'lg', 'nvidia', 'intel', 'amd']
new_users = ['amd', 'qualcomm', 'nvidia', 'logitech', 'hyperx'] 

for new_user in new_users:
    if new_user in current_users:
        print("Sorry, this username is taken. Please enter a new username.")
    else:
        print(f"{new_user} username is available.")

# 5-11 Ordinal numbers: Ordinal numbers indicate their position in a list, such as 1st or 2nd. Most ordinal numbers end in th, except 1, 2, and 3.
numbers = list(range(1, 10))
print(numbers)

## Loop through the list and use an if-elif-else chain.
## Output should read "1st 2nd 3rd 4th 5th 6th 7th"
for number in numbers:
    if number == 1:
        print("1st")
    elif number == 2:
        print("2nd")
    elif number == 3:
        print("3rd")
    else:
        print(f"{number}th")
    