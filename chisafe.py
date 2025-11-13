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