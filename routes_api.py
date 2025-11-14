import requests
from secrets import GEOAPIFY_API_KEY
from geo import zip_to_coords

def get_route_options(origin_zip, destination_zip):
    origin_coords = zip_to_coords
    dest_coords = zip_to_coords(destination_zip)

    if origin_coords is None or dest_coords is None:
        return ( 
            "route_name": "Unknown",
            "distance_mi": 0,
            "estimated_time_min": 0
        )

    lat1, lon1 = origin_coords
    lat2, lon2 = dest_coords

    url = "https://api.geoapify.com/v1/routing"
    params = {
        "waypoints": f"{lat1},{lon1}|{lat2},{lon2}",
        "mode": "drive",
        "apiKey": GEOAPIFY_API_KEY
    }