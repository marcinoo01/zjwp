from api.weather_stat_details import WeatherDataProcessor
from api.weather_processing import fetch_weather_data, retrieve_weather_instance
from api.weather_util import map_weather, import_from_file_to_list
from api.weather_enum import WeatherFields
from api.weather_data_presenter import WeatherPresenter
from api.weather_linear_regression import WeatherLinearRegression

import streamlit as st

WEATHER_DATA = "weather_data"

if WEATHER_DATA not in st.session_state:
    st.session_state[WEATHER_DATA] = []

st.title("Weather Analysis App")
st.write("Input location name")

location = st.text_input("City name:")

if st.button("Load Data"):
    if location.strip():
        try:
            weather_rq = fetch_weather_data(location)
            weather = retrieve_weather_instance(weather_rq)
            st.session_state[WEATHER_DATA].append(map_weather(weather))
        except Exception as e:
            st.error(f"Error: {e}")

uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])
if uploaded_file:
    try:
        new_data = import_from_file_to_list(uploaded_file, st.session_state[WEATHER_DATA])
        st.session_state[WEATHER_DATA].extend(new_data)
    except Exception as e:
        st.error(f"Import data error: {e}")

if st.session_state[WEATHER_DATA]:
    processor = WeatherDataProcessor(st)
    weather_stats = processor.calculate_statistics()
    WeatherPresenter.display_weather_statistics(weather_stats, st)
    df = processor.df

    if weather_stats.min_temp != weather_stats.max_temp:
        min_temp_filter = st.slider(
            "Filter by Minimum Temperature (°C):",
            min_value=int(df[WeatherFields.TEMPERATURE].min()),
            max_value=int(df[WeatherFields.TEMPERATURE].max()),
            value=int(df[WeatherFields.TEMPERATURE].min())
        )
        max_temp_filter = st.slider(
            "Filter by Maximum Temperature (°C):",
            min_value=int(df[WeatherFields.TEMPERATURE].min()),
            max_value=int(df[WeatherFields.TEMPERATURE].max()),
            value=int(df[WeatherFields.TEMPERATURE].max())
        )

        df_filtered_temp = df[
            (df[WeatherFields.TEMPERATURE] >= min_temp_filter) &
            (df[WeatherFields.TEMPERATURE] <= max_temp_filter)
            ]

        st.subheader("Filtered Data by Temperature Range")
        st.dataframe(df_filtered_temp.style.hide(axis="index"))

        selected_location = st.selectbox(
            "Choose a location:",
            options=df_filtered_temp[WeatherFields.LOCATION].unique()
        )

        filtered_df = df_filtered_temp[df_filtered_temp[WeatherFields.LOCATION] == selected_location]

        if len(filtered_df) > 1:
            processor = WeatherLinearRegression(filtered_df)
            model_stats = processor.calculate_model_statistics()
            WeatherPresenter.display_model_statistics(model_stats, st)
            fig = processor.plot_model(model_stats)
            st.pyplot(fig)

        else:
            st.write("Not enough data for analysis.")
