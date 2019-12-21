# 4-13 Buffet: A buffet-style restaurant offers only five basic foods.
foods = ('steak', 'lobster', 'chicken', 'fried rice', 'crab')
for food in foods:
    print(food)

# Try to modify one of the items to verify Python rejects the change of tuple.
## foods[1] = 'shrimp'

# Modified tuple of foods
print("\nHere is the modified food menu:")
foods = ('steak', 'snake', 'chicken', 'cake', 'crab')
for food in foods:
    print(food)