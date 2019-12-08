# 6-1 Person: Use a dictionary to store information about a person.
# Store first name, last name, age, and the city in which they live.
person = {'first_name': 'tyson', 'last_name': 'nguyen', 'age': 21, 'city': 'beaverton'}

print(person['first_name'].title())
print(person['last_name'].title())
print(person['age'])
print(person['city'].title())

# 6-2 Favorite Numbers: Use a dictionary to store 5 people's favorite number.
# Use the names as keys and store each number in as a value.
favorite_numbers = {
    'lillard': 0,
    'collins': 33,
    'mccollum': 3,
    'nurkic': 27,
    'hood': 5
}

print(f"Lillard's number is {favorite_numbers['lillard']}.")
print(f"McCollum's number is {favorite_numbers['mccollum']}.")
print(f"Hoods's number is {favorite_numbers['hood']}.")
print(f"Collin's number is {favorite_numbers['collins']}.")
print(f"Nurkic's number is {favorite_numbers['nurkic']}.")

# 6-3 Glossary: A Python dictionary can be used to model an actual dictionary.
# Think of five programming words learned in previous chapters, and store meanings as values.
glossary = {
    'boolean': 'A binary variable having two possible values True or False.',
    'list comprehension': 'Combines a for loop and the creation of new elements into one line, and automatically appends each new element.',
    'tuple': 'Refers to values in a list that cannot change as immutable.',
    'immutable': 'A value that cannot be changed in place after assignment or initialization.',
    'list': 'A collection of items in a particular order.'
}

print(f"Boolean: \n\t{glossary['boolean']}")
print(f"List comprehension: \n\t{glossary['list comprehension']}")
print(f"Tuple: \n\t{glossary['tuple']}")
print(f"Immutable: \n\t{glossary['immutable']}")
print(f"List: \n\t{glossary['list']}")