from transit import get_transit_data
from stations import get_nearest_station
from geo import zip_to_coords
from weather_api import get_weather_data
from crime_api import get_crime_data
from routes_api import get_route_options
from risk import calculate_risk_score, get_risk_label


def get_user_input():
    print("ChiSafe Commute")
    origin_zip = input("Enter your origin ZIP code: ")
    destination_zip = input("Enter your destination ZIP code: ")
    return origin_zip, destination_zip


def main():

  origin_zip, destination_zip = get_user_input()

  weather = get_weather_data(origin_zip)
  crime = get_crime_data(origin_zip, destination_zip)
  route = get_route_options(origin_zip, destination_zip)

  #finds the nearest station based on the orgin provided 
  coords = zip_to_coords(origin_zip)
  print("DEBUG coords:", coords)


  if coords is None:
      station_name = "Unknown"
      transit = {"delays_minutes": 0, "service_alerts": False}
  else:
      lat, lon = coords
      station = get_nearest_station(lat, lon)

      if station is None:
          station_name = "Unknown"
          transit = {"delays_minutes": 0, "service_alerts": False}
      else:
          station_name = station["name"]
          transit = get_transit_data(station["mapid"])

  #calculate risk score
  risk_score = calculate_risk_score(weather, crime, transit, route)
  risk_label = get_risk_label(risk_score)

  #display results
  print("\n=== Route Summary ===")
  print(f"From ZIP: {origin_zip}  To ZIP: {destination_zip}")
  print(f"Route: {route['route_name']}, Distance: {route['distance_mi']} mi, Estimated Time: {route['estimated_time_min']} min")
  print(f"Nearest CTA Station: {station_name}")

  print("\n=== Data Used ===")
  temp_f = weather["temperature"] * 9/5 + 32
  print(f"Weather: {weather['condition']}, Temp: {temp_f:.1f}°F, Alert: {weather['alert']}")
  print(f"Crime Incidents: {crime['incidents']}, High Risk Area: {crime['high_risk_area']}")
  print(f"Transit Delays: {transit['delays_minutes']} min, Service Alerts: {transit['service_alerts']}")

  print("\n=== Risk Score ===")
  print(f"Overall Risk Score: {risk_score}/100 ({risk_label})")

if __name__ == "__main__":
  main()