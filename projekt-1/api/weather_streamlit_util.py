import streamlit as st
from .weather_enum import WeatherFields
from .weather_util import import_from_file_to_list
from datetime import date

WEATHER_DATA = "weather_data"

def init():
    if WEATHER_DATA not in st.session_state:
        st.session_state[WEATHER_DATA] = []

    st.title("Weather Analysis App")
    st.write("Input location name")

    location = st.text_input("City name:")
    date_input = st.date_input("Select a date for weather data:", value=date.today())

    return location, date_input


def select_date(default_date):
    return st.date_input("Select a historical date:", value=default_date)

def add_date_range_slider(df, text):
    return st.slider(
        text,
        min_value=df[WeatherFields.LOCALTIME].min().to_pydatetime(),
        max_value=df[WeatherFields.LOCALTIME].max().to_pydatetime(),
        value=(df[WeatherFields.LOCALTIME].min().to_pydatetime(), df[WeatherFields.LOCALTIME].max().to_pydatetime())
    )

def select_location(df_filtered_temp):
    return st.selectbox(
        "Choose a location:",
        options=df_filtered_temp[WeatherFields.LOCATION].unique()
    )

def add_to_session(weather_data):
    st.session_state[WEATHER_DATA].append(weather_data)
    return weather_data

def extend_weather_data(new_data):
    st.session_state[WEATHER_DATA].extend(new_data)
    return st.session_state[WEATHER_DATA]

def import_weather_data(file):
    return import_from_file_to_list(file, st.session_state[WEATHER_DATA])