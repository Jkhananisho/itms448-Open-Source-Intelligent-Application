
STATIONS = [
  {
    "name": "Clark/Lake",
    "lat": 41.885737,
    "lon": -87.631262,
    "mapid": 40380
  }
]

def get_nearest_station(lat, lon):
  if not STATIONS:
    return None
  
  best_station = None
  best_dist = None

  for station in STATIONS:
    s_lat = station["lat"]
    s_lon = station["lon"]

    d = (lat - s_lat) ** 2 + (lon - s_lon) ** 2

    if best_dist is None or d < best_dist:
      best_dist = d
      best_station = station

  return best_station