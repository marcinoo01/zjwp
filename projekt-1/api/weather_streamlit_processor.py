import pandas as pd
import streamlit as st
from .weather_data_processor import WeatherDataProcessor
from .weather_data_presenter import display_weather_statistics, display_temp_over_time, display_wind_over_temp
from .weather_streamlit_util import select_location
from .weather_plotter import plot_wind_vs_temp, plot_temp_vs_time
from .weather_streamlit_util import WEATHER_DATA, add_date_range_slider
from .weather_enum import WeatherFields
from .weather_linear_regression import perform_linear_regression

def process_weather_data():
    if st.session_state[WEATHER_DATA]:
        weather_stats, df = calculate_weather_statistics()
        display_weather_statistics(weather_stats, st)

        st.subheader("All Locations and Data")
        st.dataframe(df.style.hide(axis="index"))

        selected_location = select_location(df)
        filtered_df = filter_by_location(df, selected_location)

        perform_linear_regression(filtered_df, st)
        apply_wind_vs_time_data(filtered_df)
        apply_wind_vs_temp_data(filtered_df)

def calculate_weather_statistics():
    processor = WeatherDataProcessor(st)
    return processor.calculate_statistics(), processor.df

def filter_by_location(df_filtered_temp, selected_location):
    return df_filtered_temp[df_filtered_temp[WeatherFields.LOCATION] == selected_location]

def apply_wind_vs_time_data(df):
    st.subheader("Temperature over Time")
    df[WeatherFields.LOCALTIME] = pd.to_datetime(df[WeatherFields.LOCALTIME])

    start_date, end_date = add_date_range_slider(df, "Select Date Range for Temperature Over Time:")
    df_filtered = df[(df[WeatherFields.LOCALTIME] >= start_date) & (df[WeatherFields.LOCALTIME] <= end_date)]

    st.write(f"Selected Date Range: {start_date.strftime('%Y-%m-%d %H:%M')} to {end_date.strftime('%Y-%m-%d %H:%M')}")
    display_temp_over_time(st, df_filtered)
    plot_temp_vs_time(st, df_filtered)


def apply_wind_vs_temp_data(df):
    st.subheader("Wind Speed vs Temperature")
    df[WeatherFields.LOCALTIME] = pd.to_datetime(df[WeatherFields.LOCALTIME])
    start_date, end_date = add_date_range_slider(df, "Select Date Range for Wind Speed vs Temperature:")

    df_filtered = df[(df[WeatherFields.LOCALTIME] >= start_date) & (df[WeatherFields.LOCALTIME] <= end_date)]

    st.write(f"Selected Date Range: {start_date.strftime('%Y-%m-%d %H:%M')} to {end_date.strftime('%Y-%m-%d %H:%M')}")
    display_wind_over_temp(st, df_filtered)
    plot_wind_vs_temp(st, df_filtered)