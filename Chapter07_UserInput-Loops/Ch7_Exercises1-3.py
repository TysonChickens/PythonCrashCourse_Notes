# 7-1 Rental Car: Ask the user what kind of rental car they want.
# Print a message about that car.
car = input("What car would like? ")
print(f"\nGive me a moment while I try to find a {car.title()} for you.")

# 7-2 Restaurant Seating: Ask the user how many people are in their dinner group.
people = input("How many people are eating today? ")

## If more than 8, print a message to wait for a table. Otherwise, their table is ready.
if int(people) > 8:
    print("Sorry, all the tables are full and the wait might be awhile.")
else:
    print("There is a table ready!")

# 7-3 Multiples of Ten: Ask the user for a number, and then report whether the number is a multiple of 10.
number = input("Give me a number: ")
number = int(number)

if number % 10 == 0:
    print(str(number) + " is a multiple of 10.")
else:
    print(str(number) + " is not a multiple of 10.")
