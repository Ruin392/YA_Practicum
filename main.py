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
# # Новая функция, она возвращает правильное словосочетание, склоняя слово "друзья"
# # в зависимости от того, какое число передано в аргументе friends_count
# def format_friends_count(friends_count):
#     if friends_count == 1:
#         return '1 друг'
#     elif 2 <= friends_count <= 4:
#         return f'{friends_count} друга'
#     else:
#         return f'{friends_count} друзей'
#
#
# def process_anfisa(query):
#     if query == 'сколько у меня друзей?':
#         count = len(DATABASE)
#         # Вызовите функцию format_friends_count() и передайте в неё count.
#         # Отредактируйте строку ниже: в ней должно использоваться выражение,
#         # которое вернёт функция format_friends_count()
#         return f'У тебя {format_friends_count(count)}.'
#     elif query == 'кто все мои друзья?':
#         friends_string = ', '.join(DATABASE)
#         return f'Твои друзья: {friends_string}'
#     elif query == 'где все мои друзья?':
#         unique_cities = set(DATABASE.values())
#         cities_string = ', '.join(unique_cities)
#         return f'Твои друзья в городах: {cities_string}'
#     else:
#         return '<неизвестный запрос>'
#
#
# def process_query(query):
#     search_name = query.split(',')[0]
#     question = query.split(',')[1].strip()
#     if search_name == 'Анфиса':
#         return (process_anfisa(str(question)))
#     else:
#         return process_friend(search_name, question)
#
#
# def process_friend(name, query):
#     if name in DATABASE and query == 'ты где?':
#         city = DATABASE[name]
#         names = name
#         return f'{names} в городе {city}'
#     elif name not in DATABASE:
#         return f'У тебя нет друга по имени {name}'
#     else:
#         return '<неизвестный запрос>'
#
#
# print('Привет, я Анфиса!')
# print(process_query('Анфиса, сколько у меня друзей?'))
# print(process_query('Анфиса, кто все мои друзья?'))
# print(process_query('Анфиса, где все мои друзья?'))
# print(process_query('Анфиса, кто виноват?'))
# print(process_query('Соня, ты где?'))
# print(process_query('Коля, что делать?'))
# print(process_query('Антон, ты где?'))
import datetime
import datetime as dt

# DATABASE = {
#     'Серёга': 'Омск',
#     'Соня': 'Москва',
#     'Дима': 'Челябинск',
#     'Алина': 'Красноярск',
#     'Егор': 'Пермь'
# }
#
# UTC_OFFSET = {
#     'Санкт-Петербург': 3,
#     'Москва': 3,
#     'Самара': 4,
#     'Новосибирск': 7,
#     'Екатеринбург': 5,
#     'Нижний Новгород': 3,
#     'Казань': 3,
#     'Челябинск': 5,
#     'Омск': 6,
#     'Ростов-на-Дону': 3,
#     'Уфа': 5,
#     'Красноярск': 7,
#     'Пермь': 5,
#     'Воронеж': 3,
#     'Волгоград': 3,
#     'Краснодар': 3,
#     'Калининград': 2
# }
#
# def what_time(friend):
#    city = DATABASE[friend]
#    return (dt.timedelta(hours=UTC_OFFSET[city]) + dt.datetime.utcnow())
#
#
#
# print(what_time('Соня'))
# DATABASE = {
#     'Сергей': 'Омск',
#     'Соня': 'Москва',
#     'Алексей': 'Калининград',
#     'Миша': 'Москва',
#     'Дима': 'Челябинск',
#     'Алина': 'Красноярск',
#     'Егор': 'Пермь',
#     'Коля': 'Красноярск',
#     'Артём': 'Владивосток',
#     'Петя': 'Михайловка'
# }
#
# UTC_OFFSET = {
#     'Москва': 3,
#     'Санкт-Петербург': 3,
#     'Новосибирск': 7,
#     'Екатеринбург': 5,
#     'Нижний Новгород': 3,
#     'Казань': 3,
#     'Челябинск': 5,
#     'Омск': 6,
#     'Самара': 4,
#     'Ростов-на-Дону': 3,
#     'Уфа': 5,
#     'Красноярск': 7,
#     'Воронеж': 3,
#     'Пермь': 5,
#     'Волгоград': 3,
#     'Краснодар': 3,
#     'Калининград': 2,
#     'Владивосток': 10
# }
#
#
# def format_count_friends(count_friends):
#     if count_friends == 1:
#         return '1 друг'
#     elif 2 <= count_friends <= 4:
#         return f'{count_friends} друга'
#     else:
#         return f'{count_friends} друзей'
#
#
# def what_time(city):
#     offset = UTC_OFFSET[city]
#     city_time = dt.datetime.utcnow() + dt.timedelta(hours=offset)
#     f_time = city_time.strftime("%H:%M")
#     return f'Там сейчас {f_time}'
#
#
# def process_anfisa(query):
#     if query == 'сколько у меня друзей?':
#         count = len(DATABASE)
#         return f'У тебя {format_count_friends(count)}.'
#     elif query == 'кто все мои друзья?':
#         friends_string = ', '.join(DATABASE)
#         return f'Твои друзья: {friends_string}'
#     elif query == 'где все мои друзья?':
#         unique_cities = set(DATABASE.values())
#         cities_string = ', '.join(unique_cities)
#         return f'Твои друзья в городах: {cities_string}'
#     else:
#         return '<неизвестный запрос>'
#
#
# def process_friend(name, query):
#     if name in DATABASE:
#         city = DATABASE[name]
#         if query == 'ты где?':
#             return f'{name} в городе {city}'
#         elif query == 'который час?':
#             if name in DATABASE:
#                 if DATABASE[name] in UTC_OFFSET:
#                     return what_time(DATABASE[name])
#                 else:
#                     return f'<не могу определить время в городе {DATABASE[name]}>'
#         else:
#             return '<неизвестный запрос>'
#     else:
#         return f'У тебя нет друга по имени {name}'
#
#
# def process_query(query):
#     elements = query.split(', ')
#     if elements[0] == 'Анфиса':
#         return process_anfisa(elements[1])
#     else:
#         return process_friend(elements[0], elements[1])
#
#
# def runner():
#     queries = [
#         'Анфиса, сколько у меня друзей?',
#         'Анфиса, кто все мои друзья?',
#         'Анфиса, где все мои друзья?',
#         'Анфиса, кто виноват?',
#         'Коля, ты где?',
#         'Соня, что делать?',
#         'Антон, ты где?',
#         'Алексей, который час?',
#         'Артём, который час?',
#         'Антон, который час?',
#         'Петя, который час?'
#     ]
#     for query in queries:
#         print(query, '-', process_query(query))
#
# runner()