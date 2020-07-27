import requests


city = "Las Vegas"
country = "US"

api_key = "c57baf757ae0865afd737c0980bdca81"

weather_url = requests.get(
    f'http://api.openweathermap.org/data/2.5/weather?q={city},{country}&appid={api_key}&units=metric')

weather_data = weather_url.json()

temp = round(weather_data['main']['temp'])
humidity = weather_data['main']['humidity']
wind_speed = weather_data['wind']['speed']
