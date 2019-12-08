# 6-7 People: Make two new dictionaries representing different people.
# Store all three dictionaries in a list called people.
# Loop through your list of people and print eveything about each person.
person_0 = {'first_name': 'tyson', 'last_name': 'nguyen', 'age': 21, 'city': 'beaverton'}
person_1 = {'first_name': 'anthony', 'last_name': 'davis', 'age': 26, 'city': 'los angeles'}
person_2 = {'first_name': 'damian', 'last_name': 'lillard', 'age': 29, 'city': 'portland'}

## Store dictionaries in a list and then loop and print all information about them.
people = [person_0, person_1, person_2]

for person in people:
    name = person['first_name'].title() + " " + person['last_name'].title()
    age = str(person['age'])
    city = person['city'].title()

    print(name + " lives in " + city + " and is " + age + " years old.")
print(people)

# 6-8 Pets: Make several dictionaries where each represents a different pet.
# In each, include kind of animal and owner's name and store them in a list called pets.
pets = []

pet = {
    'animal-type': 'dog',
    'name': 'bolt',
    'owner': 'john',
    'weight': 22,
}
pets.append(pet)

pet = {
    'animal-type': 'cat',
    'name': 'felix',
    'owner': 'nancy',
    'weight': 10,
}
pets.append(pet)

pet = {
    'animal-type': 'bird',
    'name': 'express',
    'owner': 'tyler',
    'weight': 2,
}
pets.append(pet)

## Print out all the information about each pet.
for pet in pets:
    print("\nHere is " + pet['name'].title() + ":")
    for key, value in pet.items():
        print("\t" + key.title() + ":" + str(value).title())

# 6-9 Favorite Places: Make a dictionary called favorite_places with three person names as keys.
favorite_places = {
    'eric': ['rome', 'paris', 'new zealand'],
    'tiffany': ['bora bora', 'maui', 'tahiti'],
    'alex': ['phuket', 'yosemite', 'grand canyon'],
}

## Loop through dictionary and print each person's name and their favorite places.
for name, places in favorite_places.items():
    print(f"\n{name.title()}'s favorite places are:")
    for place in places:
        print(f"\t{place.title()}")


# 6-10 Favorite Numbers: Create a dictionary so each person can have more than one favorite number.
# Then print each peron's name along with their favorite numbers. 
favorite_numbers = {
    'alex': [2, 7, 10],
    'amy': [1, 5],
    'luka': [20, 11, 23],
    'chris': [1, 7],
    'phil': [50, 100],
}

for name, numbers in favorite_numbers.items():
    print(f"\nThis is {name.title()}'s favorite numbers:")
    for number in numbers:
        print("\t" + str(number))


# 6-11 Cities: Make a dictionary called cities and use the names of three cities as keys.
cities = {
    'kyoto': {
        'country': 'japan',
        'population': '1.47 million (2018)',
        'fact': 'Its historical charm and beauty lies in its many temples and shrines, parks, and gardens.',
    },
    'havana': {
        'country': 'cuba',
        'population': '2.11 million (2012)',
        'fact': 'Center of the Cuban government with homes to various ministries, headquarters of businesses and over 90 diplomatic offices.',
    },
    'chengdu': {
        'country': 'china',
        'population': '11.05 million (2016)',
        'fact': 'Is famous for being the home of giant pandas.',
    },
}

for city, info in cities.items():
    city = city.title()
    country = info['country'].title()
    population = info['population']
    fact = info['fact']

    print(f"\n{city}, {country} with a population of {population} - {fact}")


# 6-12 Extensions: Use one of the example programs from this chapter.
# Extend it by adding new keys and values, changing the context of the program or improving the formatting of the output. 
