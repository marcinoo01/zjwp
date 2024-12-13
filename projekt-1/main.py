import streamlit as st

from api.weather_processing import fetch_weather_data, retrieve_weather_instance
from api.weather_streamlit_processor import process_weather_data
from api.weather_streamlit_util import init, add_to_session, \
    extend_weather_data, import_weather_data, load_input
from api.util import compose, validate_uploaded_file
from api.weather_util import map_weather, load_weather_data

def process_uploaded_file(uploaded_file):
    process_file = compose(
        extend_weather_data,
        import_weather_data,
        validate_uploaded_file
    )
    try:
        process_file(uploaded_file)
    except Exception as exception:
        st.error(f"Import data error: {exception}")

process_weather = compose(
    add_to_session,
    map_weather,
    retrieve_weather_instance,
    fetch_weather_data,
    load_weather_data
)

init()
location = load_input()

if st.button("Load Data"):
    try:
        process_weather(location)
    except Exception as e:
        st.error(f"Error: {e}")

uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])
if uploaded_file:
    process_uploaded_file(uploaded_file)

process_weather_data()
