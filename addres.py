from geopy.geocoders import Nominatim
from typing import NamedTuple
from dataclasses import dataclass

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

if __name__ == "__main__": 
    addres = input()
    coords = get_coordinates(addres)
    latitude = coords.latitude
    longitude = coords.longitude