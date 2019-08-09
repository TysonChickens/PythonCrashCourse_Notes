# 3-8 Seeing the World: Five places in the world to visit.
five_places = ['Palawan Island, Phillipines', 'Barcelona, Spain', 'Dubai, United Arab Emirates', 'Porto, Portugal', 'London, United Kingdom']
print(f'Original list: {five_places}')

## Print and sort the list temporarily in alphabetical order using sorted().
print(f'Sorted list in alphabetical order: {sorted(five_places)}')

## Print in reverse alphabetical order with sorted().
print(f'Reverse alphabetical order: {sorted(five_places, reverse = True)}')

## Use reverse() to change order of list and print to show order has changed.
five_places.reverse()
print(five_places)

## Use reverse() again to change order back to its original.
five_places.reverse()
print(five_places)

## Use sort() to change list in alphabetical order.
five_places.sort()
print(five_places)

## Use sort() to change list in reverse alphabetical order.
five_places.sort(reverse = True)
print(five_places)

# 3-9 Dinner Guests: Print a message indicating the number of people invited to dinner.
guests = ['Bill Gates', 'Elon Musk', 'Lisa Su']

print(f'I originally invited {len(guests)} people to dinner.')

# 3-10 Every Function: Create a list using every function introduced in the chapter.
states_no_tax = ['Alaska', 'Oregon', 'Seattle', 'Delaware', 'Montana', 'New Jersey']
print(sorted(states_no_tax))

del states_no_tax[-1]
states_no_tax.remove('Seattle')
states_no_tax.append('New Hampshire')
states_no_tax.sort()

print(states_no_tax)
print('Seattle is removed because it is a city and New Jersey (has sales tax) is replaced with New Hampshire.')
print(f'There should only by {len(states_no_tax)} states with no sales tax in the United States.')