# 7-8 Deli: Make a list called sandwich_orders filled with names of various sandwiches.
sandwich_orders = ['plain', 'bacon', 'cheese', 'tuna', 'ham', 'egg']

# Empty list for finished sandwiches.
finished_sandwiches = []

# Move each sandwich from sandwich_orders to finished_sandwiches.
while sandwich_orders:
    sandwich = sandwich_orders.pop()
    print("I am currently processing your " + sandwich + " sandwich. Please wait...")
    finished_sandwiches.append(sandwich)

# Display all finished sandwiches.
for sandwich in finished_sandwiches:
    print("I finished making your " + sandwich + " sandwich. Enjoy!")


# 7-9 No Pastrami: Using the list sandwich_orders, make sure to remove pastrami sandwiches from orders.
sandwich_orders = ['pastrami', 'plain', 'bacon', 'cheese', 'pastrami', 'tuna', 'ham', 'pastrami', 'egg']

# Notify we ran out of pastrami.
print("Sorry, the deli has run out of pastrami.")

# Remove all instances of pastrami orders.
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

# Display the new orders without pastrami.
print(sandwich_orders)


# 7-10 Dream vacation: Write a program that polls users about their dream vacation.
name_prompt = "\nWhat is your name? "
travel_prompt = "If you could visit one place in the world, where would you go? "
continue_prompt = "Would you like someone else to respond? (yes/no) "

# Store the responses {name: place}.
responses = {}

while True:
    # Ask the user where to visit.
    name = input(name_prompt)
    place = input(travel_prompt)

    # Store the response.
    responses[name] = place
    
    # Ask if someone else to respond.
    repeat = input(continue_prompt)
    if repeat == 'no':
        break

# Show the results.
print("\nHere are the results:")
for name, place in responses.items():
    print(name.title() + " would visit " + place.title() + ".")
