# Wheather Notification System using Python
# Developed by: Kiran Bala

import requests
from plyer import notification

# Step 1: Enter city name
city = "Jalandhar"

# Step 2: Get coordinates of the city
geo_url = "https://geocoding-api.open-meteo.com/v1/search"
geo_params = {"name": city, "count": 1}

geo_res = requests.get(geo_url, params=geo_params).json()

if "results" in geo_res:

    # Step 3: Get latitude and longitude
    lat = geo_res["results"][0]["latitude"]
    lon = geo_res["results"][0]["longitude"]

    # Step 4: Get current weather
    weather_url = "https://api.open-meteo.com/v1/forecast"
    weather_params = {
        "latitude": lat,
        "longitude": lon,
        "current_weather": True
    }

    weather_res = requests.get(weather_url, params=weather_params).json()

    if "current_weather" in weather_res:

        # Step 5: Store temperature and wind speed
        temp = weather_res["current_weather"]["temperature"]
        wind = weather_res["current_weather"]["windspeed"]

        # Step 6: Create weather message
        weather_info = f"{city}\nTemperature: {temp}°C\nWind Speed: {wind} km/h"

        print("Current Weather Report")
        print(weather_info)

        # Step 7: Show desktop notification
        notification.notify(
            title="Weather Update",
            message=weather_info,
            timeout=5
        )

    else:
        print("Weather data not found.")

else:
    print("City not found.")
