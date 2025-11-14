import requests
from geo import zip_to_coords

def get_weather_data(zipcode):
    coords = zip_to_coords(zipcode)

    if coords is None:
        print("Using default weather (ZIP lookup failed).")
        return {
            "condition": "Unknown",
            "temperature": 70,
            "alert": False
        }

    lat, lon = coords

    url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true"

    try:
        response = requests.get(url)
        data = response.json()

        temperature = data["current_weather"]["temperature"]
        weather_code = data["current_weather"]["weathercode"]

        condition_map = {
            0: "Clear",
            1: "Mainly Clear",
            2: "Partly Cloudy",
            3: "Overcast",
            45: "Fog",
            48: "Depositing Rime Fog",
            51: "Light Drizzle",
            53: "Moderate Drizzle",
            55: "Dense Drizzle",
            61: "Light Rain",
            63: "Moderate Rain",
            65: "Heavy Rain",
            71: "Light Snow",
            73: "Moderate Snow",
            75: "Heavy Snow",
            80: "Rain Showers",
            81: "Heavy Rain Showers",
            95: "Thunderstorm"
        }

        condition = condition_map.get(weather_code, "Unknown")

        alert = weather_code >= 61 or weather_code == 95

        return {
            "condition": condition,
            "temperature": temperature,
            "alert": alert
        }

    except:
        print("Weather API failed. Using fallback.")
        return {
            "condition": "Unknown",
            "temperature": 70,
            "alert": False
        }