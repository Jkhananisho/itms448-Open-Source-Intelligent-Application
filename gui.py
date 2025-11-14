import tkinter as tk
from tkinter import messagebox

from transit import get_transit_data
from stations import get_nearest_station
from geo import zip_to_coords
from weather_api import get_weather_data
from crime_api import get_crime_data
from routes_api import get_route_options
from risk import calculate_risk_score, get_risk_label