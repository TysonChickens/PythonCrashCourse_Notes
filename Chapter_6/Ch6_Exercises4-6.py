# 6-4 Glossary 2: A Python dictionary can be used to model an actual dictionary.
# Loop through dictionary's keys and values from glossary of words.
glossary = {
    'boolean': 'A binary variable having two possible values True or False.',
    'list comprehension': 'Combines a for loop and the creation of new elements into one line, and automatically appends each new element.',
    'tuple': 'Refers to values in a list that cannot change as immutable.',
    'immutable': 'A value that cannot be changed in place after assignment or initialization.',
    'list': 'A collection of items in a particular order.',
    'set': 'A collection in which each item must be unique.',
    'string': 'A series of characters inside quotes.',
    'comments': 'Useful feature in programming langauges to describe code with notes',
    'variables': 'Labels that can be assigned to values and store them.',
    'dictionary': 'A collection of key-value pairs.'    
    }

for word, definition in glossary.items():
    print(f"{word.title()}: \n\t{definition}")

# 6-5 Rivers: Make a dictionary containing three major rivers and the country each river runs.
rivers = {
    'mississippi': 'united states',
    'zambezi': 'zambia',
    'yangtze': 'china',
    }

for river, country in rivers.items():
    print("The " + river.title() + " flows through " + country.title() + ".")

print("\nAll the rivers in this dictionary:")
for river in rivers.keys():
    print("- " + river.title())

print("\nAll the countries in this dictionary:")
for country in rivers.values():
    print("- " + country.title())

# 6-5 Polling: Favorite languages poll

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }

for name, language in favorite_languages.items():
    print(name.title() + "'s favorite langauge is " + language.title() + ".")

friends = ['phil', 'tyson', 'alex', 'sarah', 'jen', 'edward']

for friend in friends:
    if friend in favorite_languages.keys():
        print(f"\t{friend.title()}, thank you for your response!")
    else:
        print(f"\t{friend.title()}, please respond to this poll.")
