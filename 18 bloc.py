# import requests
# import json  # импортируем необходимую библиотеку
#
# r = requests.get('https://baconipsum.com/api/?type=meat-and-filler')
# texts = json.loads(r.content)  # делаем из полученных байтов python объект для удобной работы
# print(type(texts))  # проверяем тип сконвертированных данных
#
# for text in texts:  # выводим полученный текст. Но для того чтобы он влез в консоль оставим только первые 50 символов.
#     print(text[:50], '\n')
# *************************************
# import requests
# import json
#
# r = requests.get('https://api.github.com')
#
# d = json.loads(r.content)  # делаем из полученных байтов python объект для удобной работы
#
# print(type(d))
# print(d['following_url'])  # обращаемся к полученному объекту как к словарю и попробуем напечатать одно из его значений
# *****************************
# import requests
#
# r = requests.post('https://httpbin.org/post', data={'key': 'value'})  # отправляем пост запрос
# print(r.content,end=' ')  # содержимое ответа и его обработка происходит так же, как и с гет-запросами, разницы никакой нет
# *****************
# import requests
# import json
# #программу, которая отправляет запрос на генерацию случайных текстов (используйте этот сервис).
# # Выведите первый из сгенерированных текстов.
# r = requests.get('https://baconipsum.com/api/?type=meat-and-filler')
#
# r = json.loads(r.content)
#
# print(r[0])
