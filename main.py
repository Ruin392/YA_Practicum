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

# def show_meteo(temperature, weather):
#     print(f'Сейчас {weather}, на градуснике {temperature}.')
# show_meteo(24, 'облачно')


# n = int(6953265490845412370018)
# max_digit = -1
# not_del_3 = []
# for i in str(n):
#
#     digit = int(i) % 10
#     if digit % 3 == 0 and digit > max_digit:
#         max_digit = digit
#     else:
#         not_del_3.append(digit)
#
# if len(str(n)) == len(not_del_3):
#     print('NO')
# else:
#     print(max_digit)
#
# a = int(input())
# i = 1
# while i <= a:
#     for j in range(1, 10):
#         b = i + j
#         print(f'{i} + {j} = {b}')
#     print()
#     i += 1

# n = 5
#
# for i in range(1,n+1):
#    if i <= n//2+1:
#       for j in range(i):
#          print('*',end='')
#    elif i >n//2+1:
#       for j in range(0,n-i+1):
#          print('*',end='')
#    print()
# a = int(input())
# res = []
# res.append(a)
# for i in range(0, a):
#     b = int(input())
#     res.append(b)
# print(sorted(set(res), reverse=True)[0])
# print(sorted(set(res), reverse=True)[1])




# for
# res = []
# for i in a:
#     res.append(i)
# print(sorted(set(res), reverse=True)[0])
# print(sorted(set(res), reverse=True)[1])
# enter = 0
# d_d = 0
# while enter != 10:
#     a = int(input())
#     if a % 2 == 0:
#         d_d += 1
#     enter +=1
# if d_d == enter:
#     print('YES')
# else:
#     print('NO')
# n = 0
# k = 0
# m = 0
# while n != 1 and k!=4 and m!=7:
#     for n in range(1, 29):
#         for k in range(1, 31):
#             for m in range(1, 32):
#                 if 28*n + 30*k + 31*m == 365:
#                     print(f'n = {n} k = {k} m = {m}')
#         break


# p = [x ** 5 for x in range(151)]
# pw = set(p)
# for a in range(1, 151):
#     for b in range(a, 151):
#         for c in range(b, 151):
#             for d in range(c, 151):
#                 s = p[a] + p[b] + p[c] + p[d]
#                 if s in pw:
#                     print(a, b, c, d, p.index(s))
#                     print(a + b + c + d + p.index(s))

import sqlite3


connector =  sqlite3.connect('db_ya.sqlite')
cur = connector.cursor()
#
# directors = [
#     (1, 'Текс Эйвери',1908),
#     (2, " Роберт Земякис", 1952),
#     (3, "Джерри Чинникей", 1912),
# ]
# movies = [
#     (2, 'Веселые мелоднии', "Мультсериал",1930 ),
#     (3, "Кто подставил кролика Роджера", "Фильм", 1988),
#     (4, "Безумные мелодии Луни Тюнз", "Мультсериал",1931),
#     (5, "Розовая Пантера: Контроль за вредителями", "Мультфильм", 1969),
#
# ]
# cur.executemany('INSERT INTO directors VALUES(?, ?, ?);', directors)
# cur.executemany('INSERT INTO movies VALUES(?, ?, ?, ?);', movies)
cur.execute('''
SELECT name,
       release_year
FROM movies
WHERE release_year > 1980;
''')
for result in cur:
    print(result)



# Применяем запросы.
# Запросы, переданные в cur.execute(), не будут выполнены до тех пор,
# пока не вызван метод commit().
connector.commit()
# Закрываем соединение с БД.
connector.close()