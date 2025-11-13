import requests
from secrets import CTA_TRAIN_API_KEY
from secrets import CTA_BUS_API_KEY


def get_transit_data(station_id):

  try: 
    url = (
          "https://lapi.transitchicago.com/api/1.0/ttarrivals.aspx"
          f"?key={CTA_TRAIN_API_KEY}&mapid={station_id}&outputType=JSON"
      )
    
    response = requests.get(url)

    if response.status_code != 200:
        return {"delays_minutes": 0, "service_alerts": 0}
    
    data = response.json()
    arrivals = data.get("ctatt", {}).get("eta", [])

    delays = 0
    alerts = 0

    for t in arrivals:
       if t.get("isDly") == "1":
           delays += 5

       if t.get("isApp") == "0" and t.get("isSch") == "0":
           alerts += 1

    return {
        "delays_minutes": delays,
        "service_alerts": alerts
    }
  
  except:
    return {
        "delays_minutes": 0,
        "service_alerts": 0
    }
  
def get_bus_data(route, stop_id):
  try:
      url = (
        "http://ctabustracker.com/bustime/api/v2/getpredictions"
        f"?key={CTA_BUS_API_KEY}&rt={route}&stpid={stop_id}&format=json"
    )
      
      response = requests.get(url)

      if response.status_code != 200:
          return {"bus_delay": 0}
      
      data = response.json()
      predictions = data.get("bustime-response", {}).get("prd", [])

      if not predictions:
          return {"bus_delay": 0}
      
      delay = 0

      for p in predictions:
          if p.get("dly") == True:
              delay += 5

      return {
          "bus_delay": delay}
  except:
      return {
          "bus_delay": 0}
        