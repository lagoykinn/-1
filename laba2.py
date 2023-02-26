import requests
API = '528bb07d2544990cf21eb4e774dafd2c'
city = 'Moscow'
res = requests.get("http://api.openweathermap.org/data/2.5/weather",
             params={'q': city, 'units': 'metric', 'lang': 'ru', 'APPID': API})
data = res.json()
print(data)
print("Город:", city)
print("Погодные условия:", data['weather'][0]['description'])
print("Температура:", data['main']['temp'])
print("Минимальная температура:", data['main']['temp_min'])
print("Максимальная температура", data['main']['temp_max'])
print("Cкорость ветра", data['wind']['speed'])
print("Видимость", data["visibility"])
res = requests.get("http://api.openweathermap.org/data/2.5/forecast",
                   params={'q': city, 'units': 'metric', 'lang': 'ru', 'APPID': API})
data = res.json()
print("Прогноз погоды на неделю:")
for i in data['list']:
    print("Дата <", i['dt_txt'], "> \r\nТемпература <", '{0:+3.0f}'.format(i['main']['temp']), "> \r\nПогодные условия <", i['weather'][0]['description'], "> \r\nПогодные условия <", i['weather'][0]['description'], "> \r\n", "Скорость ветра","<", i["wind"]["speed"],"\r\n Видимость", i['visibility' ])
    print("___")