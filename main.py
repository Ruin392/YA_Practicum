# friends_names = ['Аня', 'Коля', 'Лёша', 'Лена', 'Миша']
# friends_cities = ['Владивосток', 'Красноярск', 'Москва', 'Обнинск', 'Чебоксары']
#
# # Объявлен пустой словарь, его нужно будет наполнить элементами,
# # каждый из которых составлен по схеме "имя: город"
# friends =  {}
#
# # Допишите ваш код сюда
# for i in range(0, len(friends_names)):
#     friends[friends_names[i]]=friends_cities[i]
# print('Лена живёт в городе ' + friends['Лена'])

# friends =  {
#     'Серёга': 'Омск',
#     'Соня': 'Москва',
#     'Дима': 'Челябинск',
#     'Айгуль': 'Казань',
#     'Алёна': 'Белгород',
#     'Даниил': 'Санкт-Петербург',
#     'Лев': 'Тула',
#     'Валера': 'Сыктывкар',
#     'Антон': 'Ялта',
#     'Карен': 'Краснодар'
# }
#
# for name,city in friends.items():
#     print( name,'живёт в городе',city)
# favorite_songs = {
#     'Серёга': ['Unforgiven', 'Holiday', 'Highway to hell'],
#     'Соня': ['Shake it out', 'The Show Must Go On', 'Наше лето'],
#     'Дима': ['Владимирский централ', 'Мурка', 'Третье сентября']
# }
#
# print(len(favorite_songs['Дима']))
# for i in favorite_songs['Соня']:
#     print(i)

# playlist = {
#     'Venus',
#     'Yesterday',
#     'Fireball',
#     'Time',
#     'Poison',
#     'Thunderstruck'
# }
# new_music = [
#     'Kashmir',
#     'Smoke on the Water',
#     'Bohemian Rhapsody',
#     'Zombie',
#     'Let It Be',
#     'Its My Life',
# ]
# for i in new_music:
#     playlist.add(i)
#
# print(playlist)

# friends = {
#     'Серёга': 'Омск',
#     'Соня': 'Москва',
#     'Дима': 'Челябинск',
#     'Алина': 'Хабаровск',
#     'Егор': 'Пермь'
# }
#
#
# def is_anyone_in(collection, city):
#     for friend in collection:
#         if collection[friend] == city:
#             print('В городе',city, 'живёт',friend, 'Обязательно зайду в гости!')
#         else:
#             print('В городе', collection[friend], 'у меня есть друг, но мне туда не надо.')
#
#
# is_anyone_in(friends, 'Хабаровск')
#
# DATABASE = {
#     'Серёга': 'Омск',
#     'Соня': 'Москва',
#     'Миша': 'Москва',
#     'Дима': 'Челябинск',
#     'Алина': 'Красноярск',
#     'Егор': 'Пермь',
#     'Коля': 'Красноярск'
# }
#
# def process_anfisa(query):
#     if query == 'Сколько у меня друзей?':
#         count = len(DATABASE)
#         return 'У тебя ' + str(count) + ' друзей.'
#     # Здесь проверьте, что переменная query равна строке 'Кто все мои друзья?'
#     elif query == 'Кто все мои друзья?':
#         friends_string = ''
#         friends_string += str('Твои друзья: ')
#         # Чтобы получить перечень друзей -
#         # переберите словарь DATABASE в цикле
#         for i in DATABASE:
#             friends_string += str(i) + str(' ')
#         return(friends_string)
#     elif query == 'Где все мои друзья?':
#         friends_city = 'Твои друзья в городах: '
#         for city in set(DATABASE.values()):
#             friends_city += city + str(' ')
#         return (friends_city)
#
#
# # Не изменяйте следующий код
# print('Привет, я Анфиса!')
# print(process_anfisa('Сколько у меня друзей?'))
# print(process_anfisa('Кто все мои друзья?'))
# print(process_anfisa('Где все мои друзья?'))
# DATABASE = {
#     'Серёга': 'Омск',
#     'Соня': 'Москва',
#     'Миша': 'Москва',
#     'Дима': 'Челябинск',
#     'Алина': 'Красноярск',
#     'Егор': 'Пермь',
#     'Коля': 'Красноярск'
# }
#
#
# def process_anfisa(query):
#     if query == 'Сколько у меня друзей?':
#         count = len(DATABASE)
#
#         return 'У тебя ' + str(count) + ' друзей.'
#     elif query == 'Кто все мои друзья?':
#         # Из словаря DATABASE создайте строку с помощью join();
#         # имена друзей разделите запятой и пробелом.
#         friends_string = ', '.join(DATABASE)
#         return 'Твои друзья: ' + friends_string
#     elif query == 'Где все мои друзья?':
#         unique_cities = set(DATABASE.values())
#         city = ', '.join(unique_cities)
#         return 'Твои друзья в городах: '+ city
#
#         # Из сета unique_cities создайте строку с помощью join();
#         # названия городов разделите запятой и пробелом.
# print(process_anfisa('Кто все мои друзья?'))

