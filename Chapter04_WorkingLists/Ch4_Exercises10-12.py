# 4-10: Slicing a list.
nba_players = ['Harrison Barnes', 'Jaylen Brown', 'Joe Harris', 'Kyle Kuzama', 'Kemba Walker', 'Brook Lopez', 'Khris Middleton', 'Donovan Mitchell', 'Mason Plumlee', 'Marcus Smart', 'Jayson Tatum', 'Myles Turner', 'Kemba Walker']

print("The first three players in the list:")
print(nba_players[:3])

print("\nThe three players in the middle of the list:")
print(nba_players[3:6])

print("\nThe last three players in the list:")
print(nba_players[-3:])

# 4-11: My favorite pizzas, your favorite pizzas to make a copy of the list.
my_pizzas = ['Pepperoni, Sausage, Bacon']
friend_pizzas = my_pizzas[:]

my_pizzas.append('Cheese')
friend_pizzas.append('Vegetable')

## Checking if the lists are separate from each other.
print("My favorite pizzas are:")
for pizza in my_pizzas:
    print(pizza)

print("\nMy friend's favorite pizzas are:")
for pizza in friend_pizzas:
    print(pizza)

# 4-12: More loops for foods adding and printing through list.
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

my_foods.append('cheese')
friend_foods.append('carrot')

print("My favorite foods are:")
for food in my_foods:
    print(food)

print("\nMy friend's favorite foods are:")
for food in friend_foods:
    print(food)