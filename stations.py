import csv


STATIONS = []

def load_stations():
  global STATIONS
  if STATIONS:
    return
  
  try:
    with open("cta_l_stops.csv", newline='', encoding='utf-8') as csvfile:
      reader = csv.DictReader(csvfile)
      for row in reader:
        try:
          loc = row["Location"].strip().strip("()")
          lat_str, long_str = loc.split(",")

          station = {
            "name": row["STATION_NAME"],
            "lat": float(lat_str),
            "lon": float(long_str),
            "mapid": int(row["MAP_ID"])
          }
          STATIONS.append(station)
        except Exception:
          continue
  except FileNotFoundError:
    print("no file found for csv stations")



def get_nearest_station(lat, lon):
  if not STATIONS:
    load_stations()
  
  best_station = None
  best_dist = None

  for station in STATIONS:
    dx = lat - station["lat"]
    dy = lon - station["lon"]
    dist = dx * dx + dy * dy

    if best_dist is None or dist < best_dist:
      best_dist = dist
      closest = station

  return closest