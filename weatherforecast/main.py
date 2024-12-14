"""
WEATHER FORECAST: here we use weatherforecastAPI to grab weather data from a city that the user
                  will provide to the program. for documentation or to view the JSON format used
                  by the api, visit https://openweathermap.org/forecast5

                  This code will grab weather data from the provided city, and append it to a .txt
                  file "data.txt" which has column for city, time, temperature, and condition.
"""

import requests

def get_weather(city, api_key="1fa676ddb6c81cca2ef15f0c56cb2ebc"):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={api_key}"           #more data can be accessed by modifying this url
    response = requests.get(url)
    content = response.json()
    weather_types = content["list"]
    city_name = content["city"]["name"]
    with open("./data.txt", "a") as file:
        for weather_list in weather_types:                                                      #weather_types is everything inside the 'list' dictionary within the API
            temperature = weather_list["main"]["temp"]
            datetime_text = weather_list["dt_txt"]
            condition = weather_list["weather"][0]["description"]
            file.write(f"{city_name}\t\t{datetime_text}\t\t{temperature}\t\t{condition}\n")    
    print(f"Weather data for {city_name} appended to 'data.txt'.")

get_weather("Waxahachie")