from enum import Enum

class WeatherFields(str, Enum):
    LOCATION = "location"
    NAME = "name"
    CURRENT = "current"
    REGION = "region"
    COUNTRY = "country"
    TEMPERATURE = "temperature"
    FEELS_LIKE = "feelslike"
    WIND_SPEED = "wind_speed"
    WIND_DIR = "wind_dir"
    HUMIDITY = "humidity"
    LOCALTIME = "localtime"
    VISIBILITY = "visibility"
    LATITUDE = "latitude"
    LONGITUDE = "longitude"
