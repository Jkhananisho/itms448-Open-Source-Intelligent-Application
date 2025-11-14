import requests

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