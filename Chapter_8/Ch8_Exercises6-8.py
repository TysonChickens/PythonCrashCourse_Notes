# 8-6 City Names: Write a function called city_country() that takes name of city and its country.
def city_country(city, country):
    """Return a formatted string including city and country."""
    format = city + ", " + country
    return format.title()

print(city_country('madrid', 'spain'))
print(city_country('los angeles', 'united states'))
print(city_country('shenzhen', 'china'))


# 8-7: Album: Write a function called make_album() that takes artist name and an album title.
# Add None as optional parameter to store number of songs in an album.
def make_album(artist, album_title, songs=None):
    """Builds a dictionary describing a music album with artist and an album title."""
    music_album = {
        'album title': album_title.title(), 
        'artist': artist.title(),
        }
    if songs:
        music_album['# of songs'] = songs
    return music_album

album = make_album('tyson', 'This is fun')
print(album)

album = make_album('jonas brothers', 'happiness begins')
print(album)

album = make_album('lady gaga', 'a star is born')
print(album)

album = make_album('fake artist', 'random album name', songs=10)
print(album)


# 8-8: User Albums: From the previous program from 8-7, write a while loop that allows user to enter album title and artist.
def make_album(artist, album_title, songs=None):
    """Builds a dictionary describing a music album with artist and an album title."""
    music_album = {
        'album title': album_title.title(), 
        'artist': artist.title(),
        }
    if songs:
        music_album['# of songs'] = songs
    return music_album

# Prompt the user.
title_prompt = "\nWhat album do you want to add? "
artist_prompt = "Who is the artist? "
print("Enter 'quit' at any time to stop.")

while True:
    title = input(title_prompt)
    if title == 'quit':
        break

    artist = input(artist_prompt)
    if artist == 'quit':
        break

    album = make_album(artist, title)
    print(album)

print("\nThanks for the response!")

