"""
WEATHER FORECAST: 
"""

import requests

def get_weather(city, api_key):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={api_key}"
    response = requests.get(url)
    print(response)
    content = response.json()
    print(content)

get_weather("Waxahachie", "1fa676ddb6c81cca2ef15f0c56cb2ebc")