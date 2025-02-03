from datetime import datetime
from dataclasses import dataclass
from typing import Literal, TypeAlias
from urllib.error import URLError

import urllib.request
import addres
import ssl
import config 
import json 

Celsius: TypeAlias = float

class WeatherType(str):
    THUNDERSTORM = "Гроза"
    DRIZZLE = "Изморось"
    RAIN = "Дождь"
    SNOW = "Снег"
    CLEAR = "Ясно"
    FOG = "Туман"
    CLOUDS = "Облачно"

@dataclass(slots=True, frozen=True)
class Weather:
    temperature: Celsius
    weather_type: WeatherType
    sunrise: datetime
    sunset: datetime
    city: str

def get_weather(coordinates: Coordinates) -> Weather:
    weather_response = get_weather_response(latitude=addres.latitude, longitude=addres.longitude)
    weather = parse_weather_response(openweather_response)
    return weather 

def get_weather_response(latitude:float, longitude:float) -> str:
    url = config.open_weather_url.format(
        latitude=latitude, longitude=longitude)
    try:
        return urllib.request.urlopen(url).read()
    except URLError:
        raise ApiServiceError
    
def parse_weather_response 
