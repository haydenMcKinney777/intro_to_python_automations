"""
WEATHER FORECAST: 
"""

import requests

def get_weather(city, api_key="1fa676ddb6c81cca2ef15f0c56cb2ebc"):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={api_key}"
    response = requests.get(url)
    content = response.json()
    weather_types = content["list"]
    city_name = content["city"]["name"]
    weather_summary = []
    # for weather in weather_types:
    #     weather_summary.append(weather)
    # return weather_summary

    with open("./data.txt", "a") as file:
        for weather_list in weather_types:
            temperature = weather_list["main"]["temp"]
            datetime_text = weather_list["dt_txt"]
            condition = weather_list["weather"][0]["description"]
            file.write(f"{city_name},{datetime_text},{temperature},{condition}\n")    
    print(f"Weather data for {city_name} appended to 'data.txt'.")

get_weather("Waxahachie")