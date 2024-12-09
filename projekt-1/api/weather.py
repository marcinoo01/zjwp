from .weather_enum import WeatherFields

class Weather:
    """
    class representing weather structure
    """

    def __init__(self, location, country, region, temperature, feels_like, wind_speed, wind_dir, pressure, humidity, visibility, localtime):
        self.location = location
        self.country = country
        self.region = region
        self.temperature = temperature
        self.feels_like = feels_like
        self.wind_speed = wind_speed
        self.wind_dir = wind_dir
        self.pressure = pressure
        self.humidity = humidity
        self.visibility = visibility
        self.localtime = localtime

    def __str__(self):
        """
        :return:
            string representation of weather
        """
        return (f"Pogoda dla {self.location}, {self.region}, {self.country}:\n"
                f"Temperatura: {self.temperature}°C, Odczuwalna: {self.feels_like}°C\n"
                f"Wiatr: {self.wind_speed} km/h z kierunku {self.wind_dir}\n"
                f"Ciśnienie: {self.pressure} hPa\n"
                f"Wilgotność: {self.humidity}%\n"
                f"Widoczność: {self.visibility} km\n"
                f"Czas lokalny: {self.localtime}")

    @classmethod
    def from_json(self, data):
        """
        :param data:
        :return:
            weather objects from input json parameter
        """
        return self(
            location=data[WeatherFields.LOCATION][WeatherFields.NAME],
            country=data[WeatherFields.LOCATION][WeatherFields.COUNTRY],
            region=data[WeatherFields.LOCATION][WeatherFields.REGION],
            temperature=data[WeatherFields.CURRENT][WeatherFields.TEMPERATURE],
            feels_like=data[WeatherFields.CURRENT][WeatherFields.FEELS_LIKE],
            wind_speed=data[WeatherFields.CURRENT][WeatherFields.WIND_SPEED],
            wind_dir=data[WeatherFields.CURRENT][WeatherFields.WIND_DIR],
            pressure=data[WeatherFields.CURRENT][WeatherFields.HUMIDITY],
            humidity=data[WeatherFields.CURRENT][WeatherFields.HUMIDITY],
            visibility=data[WeatherFields.CURRENT][WeatherFields.VISIBILITY],
            localtime=data[WeatherFields.LOCATION][WeatherFields.LOCALTIME]
        )

    def __eq__(self, other):
        if isinstance(other, Weather):
            return self.location.lower() == other.location.lower()
        return False

    def __hash__(self):
        return hash(self.location.lower())
