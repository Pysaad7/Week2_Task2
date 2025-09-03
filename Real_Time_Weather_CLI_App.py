import requests
import json
# Need to sign up on OpenWeatherMap to get your own API key
Api = "0c599ed75895850aaf65df439e948c72"  
base_url = "http://api.openweathermap.org/data/2.5/weather"
city_name = input("Enter city name: ")
params = {"q": city_name, "appid": Api, "units": "metric"}
# GET request 
response = requests.get(base_url, params=params)
x = response.json()
# Check if the request was successful
if response.status_code == 200:
    print(f"\nWeather in {x['name']}:")
    print(f" Temperature: {x['main']['temp']}°C")
    print(f" Condition: {x['weather'][0]['description']}")
    print(f" Humidity: {x['main']['humidity']}%")
    print(f" Wind Speed: {x['wind']['speed']} m/s")
else:
    print("Error:", x.get("message", "Something went wrong"))
    # Example: city not found