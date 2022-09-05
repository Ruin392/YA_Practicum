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

# import sqlite3
#
# con = sqlite3.connect('db.sqlite')
# cur = con.cursor()
#
# cur.execute('''
# SELECT movies.name,
#        slogans.name,
#        types.name
# FROM movies
# JOIN slogans ON movies.slogan_id = slogans.id
# JOIN types ON movies.type_id = types.id;
#
# ''')
#
#
#
# for result in cur:
#     print(result)
# con.commit()
# con.close()
# def print_text(text, num):
#     while num > 0:
#         print(text, end='')
#         num -= 1
#
# print_text('Python', 4)

# def draw_triangle(fill, base):
#     for i in range(1, base + 1):
#         if i <= base // 2 + 1:
#             for j in range(i):
#                 print(fill, end='')
#         elif i > base // 2 + 1:
#             for j in range(0, base - i + 1):
#                 print(fill, end='')
#         print()
# fill = input()
# base = int(input())
# draw_triangle(fill, base)


# # объявление функции
# def get_factors(num):
#     c = 0
#     for i in range(1,num+1):
#         if num % i == 0:
#             c +=1
#     return c
#
# # считываем данные
# n = int(input())
#
# # вызываем функцию
# print(get_factors(n))

# class Contact:
#     def __init__(self, name, phone, address, birthday):
#         self.name = name
#         self.phone = phone
#         self.address = address
#         self.birthday = birthday
#         print(f"Создаём новый контакт {name}")
#
#
# # здесь создайте объекты mike и vlad
# mike = Contact('Михаил Булгаков', '2-03-27', 'Россия, Москва, Большая Пироговская, дом 35б, кв. 6', '15.05.1891')
# vlad = Contact('Владимир Маяковский', '73-88', 'Россия, Москва, Лубянский проезд, д. 3, кв. 12', '19.07.1893')
#
#
# def print_contact():
#     print(f"{mike.name} — адрес: {mike.address}, телефон: {mike.phone}, день рождения: {mike.birthday}")
#     print(f"{vlad.name} — адрес: {vlad.address}, телефон: {vlad.phone}, день рождения: {vlad.birthday}")
#
# # здесь вызовите функцию print_contact(),
# print_contact()
# # и она напечатает на экране данные контактов mike и vlad
# class Contact:
#     def __init__(self, name, phone, birthday, address):
#         self.name = name
#         self.phone = phone
#         self.birthday = birthday
#         self.address = address
#         print(f"Создаём новый контакт {name}")
#
#
# mike = Contact("Михаил Булгаков", "2-03-27", "15.05.1891", "Россия, Москва, Большая Пироговская, дом 35б, кв. 6")
# vlad = Contact("Владимир Маяковский", "73-88", "19.07.1893", "Россия, Москва, Лубянский проезд, д. 3, кв. 12")
#
#
# def print_contact():
#     print(f"{mike.name} — адрес: {mike.address}, телефон: {mike.phone}, день рождения: {mike.birthday}")
#     print(f"{vlad.name} — адрес: {vlad.address}, телефон: {vlad.phone}, день рождения: {vlad.birthday}")
#
#
# # здесь измените адрес для объекта mike
# mike.address = 'Россия, Москва, Нащокинский переулок, дом 3, кв. 44'
# # здесь измените телефон для объекта mike
# mike.phone = 'К-058-67'
#
# # здесь измените адрес для объекта vlad
# vlad.address = 'Россия, Москва, Гендриков переулок, дом 15, кв. 5'
# # здесь измените телефон для объекта vlad
# vlad.phone = '2-35-71'
#
# print_contact()  # выводим данные на экран
# class Contact:
#     def __init__(self, name, phone, birthday, address):
#         self.name = name
#         self.phone = phone
#         self.birthday = birthday
#         self.address = address
#         print(f"Создаём новый контакт {name}")
#     def show_contact(self):
#         print(f"{self.name} — адрес: {self.address}, телефон: {self.phone}, день рождения: {self.birthday}")
#
#     # def __str__(self):
#
#
#
# mike = Contact("Михаил Булгаков", "2-03-27", "15.05.1891", "Россия, Москва, Большая Пироговская, дом 35б, кв. 6")
# vlad = Contact("Владимир Маяковский", "73-88", "19.07.1893", "Россия, Москва, Лубянский проезд, д. 3, кв. 12")
#
# mike.show_contact()
# vlad.show_contact()

# импортируйте библиотеку math
# import math
#
# class Planet:
#     def __init__(self, name, radius, temp_celsius):
#         self.name = name
#         self.surface_area = 4 * math.pi * radius**2
#         self.average_temp_celsius = temp_celsius
#         self.average_temp_fahrenheit = (temp_celsius * 9/5) + 32
#
#     def show_info(self):
#         print(f"Планета {self.name} имеет площадь поверхности {self.surface_area} кв.км.")
#         print(f"Средняя температура поверхности планеты: {self.average_temp_fahrenheit} по Фаренгейту.")
#
#
# jupiter = Planet('Юпитер', 69911, -108)
# # вызовите метод show_info для Юпитера
# jupiter.show_info()

# импортируем функции из библиотеки math для рассчёта расстояния
# from math import radians, sin, cos, acos
#
#
# class Point:
#     def __init__(self, latitude, longitude):
#         self.latitude = radians(latitude)
#         self.longitude = radians(longitude)
#
#     # считаем расстояние между двумя точками в км
#     def distance(self, other):
#         cos_d = sin(self.latitude) * sin(other.latitude) + cos(self.latitude) * cos(other.latitude) * cos(
#         self.longitude - other.longitude)
#
#         return 6371 * acos(cos_d)
#
#
# class City(Point):
#     def __init__(self, latitude, longitude, name, population):
#         super().__init__(latitude, longitude)
#         # допишите код: сохраните свойства родителя
#         # и добавьте свойства name и population
#         self.name = name
#         self.population = population
#
#     def show(self):
#         print(f"Город {self.name}, население {self.population} чел.")
#
#
# class Mountain(Point):
#     def __init__(self, latitude, longitude, name, height):
#         super().__init__(latitude, longitude)
#         self.name = name
#         self.height = height
#     # допишите код: напишите конструктор, в нём сохраните свойства родителя
#     # и добавьте свойства name и height
#
#     def show(self):
#         print(f'Высота горы {self.name} - {self.height} м.')
#     # Создайте метод show(self):
#     # информацию о горе нужно вывести в формате:
#     # "Высота горы <название> - <высота> м."
#
#
# # эта функция печатает расстояние
# # между двумя любыми наследниками класса Point
# def print_how_far(geo_object_1, geo_object_2):
#     print(f'От точки «{geo_object_1.name}» до точки «{geo_object_2.name}» — {geo_object_1.distance(geo_object_2)} км.')
#
#
# # основной код
# moscow = City(55.7522200, 37.6155600, 'Москва', 12615882)
# everest = Mountain(27.98791, 86.92529, 'Эверест', 8848)
# chelyabinsk = City(55.154, 61.4291, 'Челябинск', 1200703)
#
# moscow.show()
# everest.show()
# print_how_far(moscow, everest)
# # print_how_far(moscow, chelyabinsk)
# class Human:
#     def __init__(self, name):
#         self.name = name
#
#     # ответ по умолчанию для всех одинаковый, можно
#     # доверить его родительскому классу
#     def answer_question(self, question):
#         print('Очень интересный вопрос! Не знаю.')
#
# class Student(Human):
#     #  метод ask_question() принимает параметр someone:
#     #  это объект, экземпляр класса Curator, Mentor или CodeReviewer,
#     #  которому Student задаёт вопрос;
#     #  параметр question — это просто строка
#     #  имя объекта и текст вопроса задаются при вызове метода ask_question
#     def ask_question(self, someone, question):
#         # напечатайте на экран вопрос в нужном формате
#         print(f'{someone.name}, {question}')
#         someone.answer_question(question)
#
#         print()  # этот print выводит разделительную пустую строку
#
#
# class Curator(Human):
#     def answer_question(self, question):
#         if question == 'мне грустненько, что делать?':
#             print('Держись, всё получится. Хочешь видео с котиками?')
#         else:
#             super().answer_question(question)
#
# class Mentor(Human):
#     def answer_question(self, question):
#         if question == 'мне грустненько, что делать?':
#             print('Отдохни и возвращайся с вопросами по теории.')
#         elif question == 'как устроиться работать питонистом?':
#             print('Сейчас расскажу. ')
#         else:
#             super().answer_question(question)
#
# class CodeReviewer(Human):
#     def answer_question(self, question):
#         if question == 'что не так с моим проектом?':
#             print('О, вопрос про проект, это я люблю.')
#         else:
#             super().answer_question(question)


# # следующий код менять не нужно, он работает, мы проверяли
# student1 = Student('Тимофей')
# curator = Curator('Марина')
# mentor = Mentor('Ира')
# reviewer = CodeReviewer('Евгений')
# friend = Human('Виталя')
#
# student1.ask_question(curator, 'мне грустненько, что делать?')
# student1.ask_question(mentor, 'мне грустненько, что делать?')
# student1.ask_question(reviewer, 'когда каникулы?')
# student1.ask_question(reviewer, 'что не так с моим проектом?')
# student1.ask_question(friend, 'как устроиться на работу питонистом?')
# student1.ask_question(mentor, 'как устроиться работать питонистом?')