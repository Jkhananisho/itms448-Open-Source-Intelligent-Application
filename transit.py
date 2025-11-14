import requests
from secrets import CTA_TRAIN_API_KEY
from secrets import CTA_BUS_API_KEY


def get_transit_data(mapid):

  url = "https://lapi.transitchicago.com/api/1.0/ttarrivals.aspx"
  params = {
    "key": CTA_TRAIN_API_KEY,
    "mapid": mapid,
    "outputType": "JSON"
  }

  try:
    response = requests.get(url, params=params)
    data = response.json()

    etas = data.get("ctatt", {}).get("eta", [])
    if not etas:
      return {"delays_minutes": 0, "service_alerts": False}
    
    waits = []
    delayed = False

    for eta in etas:
      prd = eta.get("prdctdn")
      if prd in ("DUE", "ARR"):
        waits.append(0)
      else:
        try:
          waits.append(int(prd))
        except:
          pass

      if eta.get("isDly") == "1":
        delayed = True

    return {
      "delays_minutes": min(waits) if waits else 0,
      "service_alerts": delayed
    }
  
  except:
    return {"delays_minutes": 0, "service_alerts": False}
  
def get_bus_data(bus_stop_id):
  return {"delays_minutes": 0, "service_alerts": False}

  