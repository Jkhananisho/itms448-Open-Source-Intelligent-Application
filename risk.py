def calculate_risk_score(weather, crime, transit, route):
  score = 100

  #crime
  score -= crime["incidents"] * 2
  if crime["high_risk_area"]:
    score -= 20

  #weather
  if weather["alert"]:
    score -= 25
  if weather["temperature"] <= -5:
    score -= 15

  #transit
  score -= transit["delays_minutes"] // 5 * 3
  if transit["service_alerts"]:
    score -= 15
  
  if score < 0:
    score = 0
  if score > 100:
    score = 100
  return score

def get_risk_label(score):
    if score < 40:
        return "High Risk"
    elif score < 70:
        return "Moderate Risk"
    else:
        return "Safer Route"