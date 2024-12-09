import pandas as pd

from .weather_enum import WeatherFields

def map_weather(weather):
    return {
        WeatherFields.LOCATION: weather.location.strip(),
        WeatherFields.REGION: weather.region.strip(),
        WeatherFields.COUNTRY: weather.country.strip(),
        WeatherFields.TEMPERATURE: weather.temperature,
        WeatherFields.FEELS_LIKE: weather.feels_like,
        WeatherFields.HUMIDITY: weather.humidity,
        WeatherFields.LOCALTIME: weather.localtime.strip(),
    }

def import_from_file_to_list(uploaded_file, data):
    imported_df = pd.read_csv(uploaded_file)
    existing_entries = {(entry[WeatherFields.LOCATION], entry[WeatherFields.LOCALTIME])
                        for entry in data}
    return list(
        filter(
            lambda row: (row[WeatherFields.LOCATION], row[WeatherFields.LOCALTIME]) not in existing_entries,
            imported_df.to_dict(orient="records")
        )
    )

