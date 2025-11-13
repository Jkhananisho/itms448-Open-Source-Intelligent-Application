def get_user_input():
  print("ChiSafe Commute")
  origin = input("Enter your origin: ")
  destination = input("Enter your destination: ")
  return origin, destination

def get_weather_data(origin, destination):
  # Placeholder for weather data retrieval logic
  weather_data = {
     "condition": "Sunny",
     "temperature": "75°F",
     "alert": False 
  }
  return weather_data

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
  # Get user input
  origin, destination = get_user_input()

  #get data from source
  weather = get_weather_data(origin, destination)
  crime = get_crime_data(origin, destination)
  transit = get_transit_data(origin, destination)
  route = get_route_options(origin, destination)

  #calculate risk score
  risk_score = calculate_risk_score(weather, crime, transit, route)

  #display results
  print("Route Summary")
  print(f"From: {origin} To: {destination}")
  print(f"Route: {route['route_name']}, Distance: {route['distance_mi']} mi, Estimated Time: {route['estimated_time_min']} min")

  print("data used")
  print(f"Weather: {weather['condition']}, Temp: {weather['temperature']}, Alert: {weather['alert']}")
  print(f"Crime Incidents: {crime['incidents']}, High Risk Area: {crime['high_risk_area']}")
  print(f"Transit Delays: {transit['delays_minutes']} min, Service Alerts: {transit['service_alerts']}")

  print(f"Overall Risk Score: {risk_score}/100")

if __name__ == "__main__":
  main()