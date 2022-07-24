def display_message():
    print('Hello')


def favorite_book(title):
    print('Your favourite book is {}'.format(title))


display_message()
favorite_book('Harry Potter')


def describe_pet(pet_name, animal_type='hamster'):
    print(f'Name: {pet_name}, and type: {animal_type}')


describe_pet(pet_name='willie')


def make_shirt(message, size='Large'):
    print(f'Shirt is {size} size, and the message on it is "{message}"')


make_shirt('Fuck you', 'medium')
make_shirt("It's okay")


def build_person(first_name, last_name, age=''):
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age
    return person


musician = build_person('jimi', 'hendrix', age=27)
print(musician)


def city_country(city, country):
    return f"{city.title()}, {country.title()}"


result = city_country('Ełk', 'Poland')
print(result)


def make_album(artist_name, album_title, number_of_songs = None):
    dict = {'artist_name': artist_name, 'album_title': album_title}
    if number_of_songs:
        dict['number_of_songs'] = number_of_songs
    return dict

album1 = make_album('Billie Joe Armstrong', 'Green Day')
album2 = make_album('Simon', 'Somebody')
album3 = make_album('Thomas', 'Break Free', 23)
print(album1)
print(album2)
print(album3)

while True:
    name = input('Tell us the name of the artist')
    album = input('Tell us the title of the album')
    songs = input('Optionally, tell us the number of songs in the album')
    if songs == '':
        songs = None

    q = ''
    answer = make_album(name, album, songs)
    print(answer)
    q = input('Do you want to continue? (yes/no)')
    if q == 'no':
        break
