from geopy.geocoders import Nominatim
from typing import NamedTuple

class Coordinates(NamedTuple):
    latitude: float
    longitude: float 

def get_coordinates(address: str) -> Coordinates:
    nominatim = Nominatim(user_agent='user')
    location = nominatim.geocode(address)
    
    if location:
        return Coordinates(latitude=location.latitude, longitude=location.longitude)
    else:
        raise ValueError("Address not found")

addres = input()
coords = get_coordinates(addres)
latitude = coords.latitude
longitude = coords.longitude