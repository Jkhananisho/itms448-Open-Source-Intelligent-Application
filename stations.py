import csv

def get_nearest_station(lat, lon):
    best_station = None
    best_dist = None

    with open("cta_l_stops.csv", "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        next(reader) 

        for row in reader:
            name = row[3]
            mapid = row[1]
            location = row[13]

            if not location or location.lower() == "false":
                continue

            location = location.strip("()")
            lat_str, lon_str = location.split(",")

            stop_lat = float(lat_str)
            stop_lon = float(lon_str)

            d = (lat - stop_lat)**2 + (lon - stop_lon)**2

            if best_dist is None or d < best_dist:
                best_dist = d
                best_station = {
                    "name": name,
                    "mapid": mapid
                }

    return best_station
