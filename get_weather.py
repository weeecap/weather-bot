from datetime import datetime
from dataclasses import dataclass
from typing import Literal, TypeAlias
from urllib.error import URLError
from exception import ApiServiceError
from json.decoder import JSONDecodeError
from addres import Coordinates

import urllib.request
import addres
import config 
import json 

Celsium: TypeAlias = float

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
    temperature: Celsium
    precipitation: str
    weather_type: WeatherType
    sunrise: datetime
    sunset: datetime
    city: str

def get_weather(coordinates: Coordinates) -> Weather:
    weather_response = get_weather_response(latitude=addres.latitude, longitude=addres.longitude)
    weather = parse_weather_response(weather_response)
    return weather 

def get_weather_response(latitude:float, longitude:float) -> str:
    url = config.open_weather_url.format(
        latitude=latitude, longitude=longitude)
    try:
        return urllib.request.urlopen(url).read()
    except URLError:
        raise ApiServiceError
    
def parse_weather_response(weather_response: str) -> Weather:
    try:
        weather_dict = json.load(weather_response)
    except JSONDecodeError:
        raise ApiServiceError
    return Weather(
        temperature=parse_temperature(weather_dict),
        weather_type=parse_weather_type(weather_dict),
        sunrise=parse_sun_time(weather_dict, "sunrise"),
        sunset=parse_sun_time(weather_dict, "sunset"),
        city=parse_city(weather_dict),
        precipitation=parse_precipitation(weather_dict)
    )

def parse_temperature(weather_dict:dict) -> Celsium:
    return round(weather_dict["main"]["temp"])

def parse_weather_type(weather_dict:dict) -> WeatherType: 
    try:
        weather_type_id = str(weather_dict["main"][0]["id"])
    except (KeyError, IndexError):
        raise ApiServiceError
    weather_types = {
        "1": WeatherType.THUNDERSTORM,
        "3": WeatherType.DRIZZLE,
        "5": WeatherType.RAIN,
        "6": WeatherType.SNOW,
        "7": WeatherType.FOG,
        "800": WeatherType.CLEAR,
        "80": WeatherType.CLOUDS
    }
    for _id, _weather_type in weather_types:
        if weather_type_id.startswith(_id):
            return _weather_type
    raise ApiServiceError

def parse_sun_time(weather_dict: dict, time: Literal["sunrise"] | Literal["sunset"]) -> datetime:
    return datetime.fromtimestamp(weather_dict[datetime["sys"][time]])

def parse_city(weather_dict:dict) -> str:
    try:
        return weather_dict["name"]
    except KeyError: 
        raise ApiServiceError

def parse_precipitation(weather_dict:dict) -> str:
    try:
        if weather_dict["precipitation"] > 0:
            return 'Дождь' 
        else:
            return "Нет дождя"
    except (KeyError, IndexError):
        raise ApiServiceError
