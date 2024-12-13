import pandas as pd
from .weather_streamlit_util import WEATHER_DATA

from .weather_enum import WeatherFields

class WeatherDataProcessor:
    def __init__(self, st):
        df = pd.DataFrame(st.session_state[WEATHER_DATA])
        df.index += 1
        self.df = df
        self._stats = None


    def calculate_statistics(self):
        self._stats = type('WeatherStats', (object,), {})()

        self._stats.avg_temp = self.df[WeatherFields.TEMPERATURE].mean()
        self._stats.avg_feels_like = self.df[WeatherFields.FEELS_LIKE].mean()

        max_temp_row = self.df.loc[self.df[WeatherFields.TEMPERATURE].idxmax()]
        self._stats.max_temp = max_temp_row[WeatherFields.TEMPERATURE]
        self._stats.hottest_location = max_temp_row[WeatherFields.LOCATION]
        self._stats.hottest_date = max_temp_row[WeatherFields.LOCALTIME]

        min_temp_row = self.df.loc[self.df[WeatherFields.TEMPERATURE].idxmin()]
        self._stats.min_temp = min_temp_row[WeatherFields.TEMPERATURE]
        self._stats.coldest_location = min_temp_row[WeatherFields.LOCATION]
        self._stats.coldest_date = min_temp_row[WeatherFields.LOCALTIME]

        self._stats.avg_humidity = self.df[WeatherFields.HUMIDITY].mean()
        self._stats.max_humidity = self.df[WeatherFields.HUMIDITY].max()
        self._stats.min_humidity = self.df[WeatherFields.HUMIDITY].min()

        self._stats.avg_wind_speed = self.df[WeatherFields.WIND_SPEED].mean()
        self._stats.max_wind_speed = self.df[WeatherFields.WIND_SPEED].max()
        self._stats.min_wind_speed = self.df[WeatherFields.WIND_SPEED].min()

        self._stats.temp_variance = self.df[WeatherFields.TEMPERATURE].var()
        self._stats.temp_std_dev = self.df[WeatherFields.TEMPERATURE].std()

        self._stats.median_temp = self.df[WeatherFields.TEMPERATURE].median()

        self._stats.record_count = len(self.df)

        return self._stats

    def filter_by_temperature(self, min_temp, max_temp):
        """
        Filters the dataframe by a temperature range.
        """
        return self.df[(self.df[WeatherFields.TEMPERATURE] >= min_temp) &
                       (self.df[WeatherFields.TEMPERATURE] <= max_temp)]

