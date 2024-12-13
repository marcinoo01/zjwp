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
        """
        Calculates various weather statistics and stores them as attributes.
        """
        self._stats = type('WeatherStats', (object,), {})()

        # Average values
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

        return self._stats

    def filter_by_temperature(self, min_temp, max_temp):
        """
        Filters the dataframe by a temperature range.
        """
        return self.df[(self.df[WeatherFields.TEMPERATURE] >= min_temp) &
                       (self.df[WeatherFields.TEMPERATURE] <= max_temp)]

