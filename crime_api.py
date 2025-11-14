import requests

def get_crime_data(origin_zip, destination_zip):
    url = "https://data.cityofchicago.org/api/v3/views/ijzp-q8t2/query.json"

    params = {
        "zip_code": origin_zip,
        "$limit": 50  
    }

    try:
        response = requests.get(url, params=params)
        data = response.json()

        incidents = len(data)

        high_risk_area = incidents >= 20

        return {
            "incidents": incidents,
            "high_risk_area": high_risk_area
        }

    except:
        return {
            "incidents": 5,
            "high_risk_area": False
        }
