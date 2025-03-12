# 2. Task: Weather API
#    1. Use this url : https://openweathermap.org/
#    2. Use the requests library to fetch weather data for a specific city(ex. your hometown: Tashkent) and print relevant information (temperature, humidity, etc.).
import requests

api = '26794b113ae569eec07479d62f6e2fe1'
city= 'Tashkent'
url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api}&units=metric'

response = requests.get(url)
data = response.json()

print('city:', data['name'])
print('weather:', data['weather'][0]['main'])
print('temp:',data['main']['temp'])
print('humidity:',data['main']['humidity'])
print('wind:',data['wind']['speed'])

