import tkinter as tk
from tkinter import messagebox

from transit import get_transit_data
from stations import get_nearest_station
from geo import zip_to_coords
from weather_api import get_weather_data
from crime_api import get_crime_data
from routes_api import get_route_options
from risk import calculate_risk_score, get_risk_label

def run_commute():
  origin_zip = origin_entry.get().strip()
  destination_zip = dest_entry.get().strip()

  if not (origin_zip.isdigit() and destination_zip.isdigit()):
      messagebox.showerror("error", "enter a real zip man")
      return
  
  try:
      weather = get_weather_data(origin_zip)
      crime = get_crime_data(origin_zip, destination_zip)
      route = get_route_options(origin_zip, destination_zip)

      coords = zip_to_coords(origin_zip)
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

      risk_score = calculate_risk_score(weather, crime, transit, route)
      risk_label = get_risk_label(risk_score)

      temp_f = weather["temperature"] * 9/5 + 32

      result_text = (
          "--- Route Summary ---\n"
          f"From ZIP: {origin_zip}  To ZIP: {destination_zip}\n"
          f"Route: {route['route_name']}, Distance: {route['distance_mi']} mi, Estimated Time: {route['estimated_time_min']} min\n"
          f"Nearest CTA Station: {station_name}\n\n"
          "--- Data Used ---\n"
          f"Weather: {weather['condition']}, Temp: {temp_f:.1f}°F, Alert: {weather['alert']}\n"
          f"Crime Incidents: {crime['incidents']}, High Risk Area: {crime['high_risk_area']}\n"
          f"Transit Delays: {transit['delays_minutes']} min, Service Alerts: {transit['service_alerts']}\n\n"
          "--- Risk Score ---\n"
          f"Overall Risk Score: {risk_score}/100 ({risk_label})"
      )

      output_box.delete(1.0, tk.END)
      output_box.insert(tk.END, result_text)

  except Exception as e:
      messagebox.showerror("Error", f"something broke: {e}")


# actual gui stuff

root = tk.Tk()
root.title("ChiSafe Commute")

tk.Label(root, text="Origin ZIP:").pack(pady=(10, 0))
origin_entry = tk.Entry(root)
origin_entry.pack(pady=5)

tk.Label(root, text="Destination ZIP:").pack(pady=(10, 0))
dest_entry = tk.Entry(root)
dest_entry.pack(pady=5)

tk.Button(root, text="Run Commute Check", command=run_commute).pack(pady=10)

output_box = tk.Text(root, height=20, width=60)
output_box.pack(pady=10)

root.mainloop()