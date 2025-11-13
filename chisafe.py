import requests

def get_user_input():
    print("ChiSafe Commute")
    origin_zip = input("Enter your origin ZIP code: ")
    destination_zip = input("Enter your destination ZIP code: ")
    return origin_zip, destination_zip

def zip_to_coords(zipcode):
    try:
        url = f"https://api.zippopotam.us/us/{zipcode}"
        response = requests.get(url)

        if response.status_code != 200:
            return None  

        data = response.json()
        lat = float(data["places"][0]["latitude"])
        lon = float(data["places"][0]["longitude"])
        return lat, lon

    except:
        return None

def get_weather_data(zipcode):
    coords = zip_to_coords(zipcode)

    if coords is None:
        print("Error finding coordinates for zip code")
        return {
            "condition": "Unknown",
            "temperature": 70,
            "alert": False
        }

    lat, lon = coords

    url = (
        f"https://api.open-meteo.com/v1/forecast?"
        f"latitude={lat}&longitude={lon}&current_weather=true"
    )

    try:
        response = requests.get(url)
        data = response.json()

        weather = data["current_weather"]
        temperature = weather["temperature"]
        conditions = weather["weathercode"]

        condition_map = {
            0: "Clear",
            1: "Mainly Clear",
            2: "Partly Cloudy",
            3: "Overcast",
            45: "Fog",
            48: "Rime Fog",
            51: "Light Drizzle",
            61: "Rain",
            80: "Rain Showers",
            95: "Thunderstorm"
        }

        condition_text = condition_map.get(conditions, "Unknown")

        return {
            "condition": condition_text,
            "temperature": temperature,
            "alert": conditions >= 80
        }

    except Exception as e:
        print("error with api")
        print("Error:", e)
        return {
            "condition": "Unknown",
            "temperature": 70,
            "alert": False
        }


def get_crime_data(origin, destination):
  # Placeholder for crime data retrieval logic
  crime_data = {
    "incidents": 5,
    "high_risk_area": False
  }
  return crime_data

def get_transit_data(origin, destination):
  # Placeholder for transit data retrieval logic
  transit_data = {
    "delays_minutes": 0,
    "service_alerts": False
  }
  return transit_data

def get_route_options(origin, destination):
  # Placeholder for route options retrieval logic
  route = {
    "route_name": "Route A",
    "distance_mi": 10,
    "estimated_time_min": 25
  }
  return route

def calculate_risk_score(weather, crime, transit, route):
  score = 100

  #crime
  score -= crime["incidents"] * 5
  if crime["high_risk_area"]:
    score -= 20

  #weather
  if weather["alert"]:
    score -= 25
  if weather["temperature"] <= -5:
    score -= 15

  #transit
  score -= transit["delays_minutes"] // 5 * 3
  if transit["service_alerts"]:
    score -= 15
  
  if score < 0:
    score = 0
  if score > 100:
    score = 100
  return score

def main():

  origin_zip, destination_zip = get_user_input()

  weather = get_weather_data(origin_zip)
  crime = get_crime_data(origin_zip, destination_zip)
  transit = get_transit_data(origin_zip, destination_zip)
  route = get_route_options(origin_zip, destination_zip)

  #calculate risk score
  risk_score = calculate_risk_score(weather, crime, transit, route)

  #display results
  print("Route Summary")
  print(f"From ZIP: {origin_zip}  To ZIP: {destination_zip}")
  print(f"Route: {route['route_name']}, Distance: {route['distance_mi']} mi, Estimated Time: {route['estimated_time_min']} min")

  print("data used")
  temp_f = weather["temperature"] * 9/5 + 32
  print(f"Weather: {weather['condition']}, Temp: {temp_f:.1f}°F, Alert: {weather['alert']}")
  print(f"Crime Incidents: {crime['incidents']}, High Risk Area: {crime['high_risk_area']}")
  print(f"Transit Delays: {transit['delays_minutes']} min, Service Alerts: {transit['service_alerts']}")

  print(f"Overall Risk Score: {risk_score}/100")

if __name__ == "__main__":
  main()