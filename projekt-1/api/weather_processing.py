import requests
from .weather import Weather

ACCESS_KEY = '2807dd46a03cd781db63334d28378b2a'

def fetch_weather_data(location):
    """
        sends rq to external weather api
    :param location:
    :return:
        json string which contains weather data
    """

    url = f"https://api.weatherstack.com/current?access_key={ACCESS_KEY}&query={location}"
    response = requests.get(url)

    if response.status_code != 200:
        raise Exception("Could not retrieve weather data")
    return response.json()


def retrieve_weather_instance(weather_data):
    """
        retrieves weather data
    :param weather_data:
    :return:
        weather instance
    """
    return Weather.from_json(data=weather_data)
