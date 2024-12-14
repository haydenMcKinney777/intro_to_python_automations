"""
WEATHER FORECAST: 
"""

import requests

def get_weather(city, api_key="1fa676ddb6c81cca2ef15f0c56cb2ebc"):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={api_key}"
    response = requests.get(url)
    content = response.json()
    weather_types = content['weather']
    weather_summary = []
    for weather in weather_types:
        weather_summary.append(weather)
    return weather_summary

weather_summary = get_weather("Waxahachie")
print(weather_summary, "\n")