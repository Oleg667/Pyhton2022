import requests
#получаем координаты города
lan_lon = requests.get('http://api.openweathermap.org/geo/1.0/direct?q=Москва&limit=5&appid=c480e28016555b89ff4d18253d8dd5ae&lang=ru')
print(lan_lon.text)
#получаем погоду по координатам
#response = requests.get('https://api.openweathermap.org/data/2.5/weather?lat=35&lon=139&appid=c480e28016555b89ff4d18253d8dd5ae')
response = requests.get('https://api.openweathermap.org/data/2.5/weather?lat=51.815809935&lon=19.6573685&appid=c480e28016555b89ff4d18253d8dd5ae&lang=ru')
print(response.text)