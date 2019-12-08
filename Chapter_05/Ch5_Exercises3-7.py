# 5-3 Alien Colors 1: An alien was shot down and check the color.
# 5-4 Aliens 2: Choose a color an alien, and use an if-else chain.
alien_color = 'blue'

if alien_color == 'green':
    print("Player has earned 5 points for shooting the alien!")

# 5-5 Aliens 3: Add more options with if-elif-else chain.
elif alien_color == 'yellow':
    print("Player has earned 10 points!")
elif alien_color == 'red':
    print("Player has earned 15 points!")
else:
    print("Player has earned 10 points!")

# 5-6 Stages of Life: Write if-elif-else chain that determines a person's stage of life.
age = 21

if age < 2:
    print("This person is a baby.")
elif age < 4:
    print("This person is a toddler.")
elif age < 13:
    print("This person is a kid.")
elif age < 20:
    print("This person is a teenager.")
elif age < 65:
    print("This person is an adult.")
else:
    print("This person is an elder.")

# 5-7 Favorite Fruit: Make a list of favorite fruits, and then write statements to check for fruits.
## Five if statements to check for certain fruits
favorite_fruits = ['bananas', 'oranges', 'watermelon']

if 'oranges' in favorite_fruits:
    print("I don't like nasty oranges with no juice.")
if 'bananas' in favorite_fruits:
    print("Bananas are my favorite fruit out of any fruit.")
if 'apples' in favorite_fruits:
    print("I do not like bad apples.")
if 'watermelon' in favorite_fruits:
    print("I love sweet juicy watermelons.")
if 'pears' in favorite_fruits:
    print("Pears are pears.")

print("I only have three favorite fruits.")


