from .weather_enum import WeatherFields

def display_model_statistics(stats, st):
    """
    Displays the regression model statistics using Streamlit.
    """
    st.write(f"- **Residual Sum of Squares (RSS)**: {stats.rss:.2f}")
    st.write(f"- **Mean Squared Error (MSE)**: {stats.mse:.2f}")
    st.write(f"- **Root Mean Squared Error (RMSE)**: {stats.rmse:.2f}")
    st.write(f"- **Mean Absolute Error (MAE)**: {stats.mae:.2f}")
    st.write(f"- Coefficient (Impact of temperature on feels-like): {stats.coefficient:.2f}")
    st.write(f"- Intercept: {stats.intercept:.2f}")
    st.write(f"- **R-squared**: {stats.r_squared:.4f}")


def display_weather_statistics(stats, st):
    """
    Displays the general weather statistics using Streamlit.
    """
    st.write(f"- **Average Temperature**: {stats.avg_temp:.2f}°C")
    st.write(f"- **Average Feels-like Temperature**: {stats.avg_feels_like:.2f}°C")
    st.write(f"- **Maximum Temperature**: {stats.max_temp}°C ({stats.hottest_location} on {stats.hottest_date})")
    st.write(f"- **Minimum Temperature**: {stats.min_temp}°C ({stats.coldest_location} on {stats.coldest_date})")
    st.write(f"- **Average Humidity**: {stats.avg_humidity:.2f}%")
    st.write(f"- **Maximum Humidity**: {stats.max_humidity:.2f}%")
    st.write(f"- **Minimum Humidity**: {stats.min_humidity:.2f}%")
    st.write(f"- **Average Wind Speed**: {stats.avg_wind_speed:.2f} km/h")
    st.write(f"- **Maximum Wind Speed**: {stats.max_wind_speed:.2f} km/h")
    st.write(f"- **Minimum Wind Speed**: {stats.min_wind_speed:.2f} km/h")
    st.write(f"- **Temperature Variance**: {stats.temp_variance:.2f}")
    st.write(f"- **Temperature Standard Deviation**: {stats.temp_std_dev:.2f}")
    st.write(f"- **Median Temperature**: {stats.median_temp:.2f}°C")
    st.write(f"- **Record Count**: {stats.record_count}")

def display_wind_over_temp(st, df_filtered):
    avg_wind_speed = df_filtered[WeatherFields.WIND_SPEED].mean()
    min_wind_speed = df_filtered[WeatherFields.WIND_SPEED].min()
    max_wind_speed = df_filtered[WeatherFields.WIND_SPEED].max()
    std_wind_speed = df_filtered[WeatherFields.WIND_SPEED].std()
    median_wind_speed = df_filtered[WeatherFields.WIND_SPEED].median()
    wind_speed_range = max_wind_speed - min_wind_speed

    st.write(f"**Wind Speed Statistics:**")
    st.write(f"- Average Wind Speed: {avg_wind_speed:.2f} km/h")
    st.write(f"- Minimum Wind Speed: {min_wind_speed:.2f} km/h")
    st.write(f"- Maximum Wind Speed: {max_wind_speed:.2f} km/h")
    st.write(f"- Standard Deviation: {std_wind_speed:.2f} km/h")
    st.write(f"- Median Wind Speed: {median_wind_speed:.2f} km/h")
    st.write(f"- Wind Speed Range: {wind_speed_range:.2f} km/h")

def display_temp_over_time(st, df_filtered):
    avg_temp = df_filtered[WeatherFields.TEMPERATURE].mean()
    min_temp = df_filtered[WeatherFields.TEMPERATURE].min()
    max_temp = df_filtered[WeatherFields.TEMPERATURE].max()
    std_temp = df_filtered[WeatherFields.TEMPERATURE].std()
    median_temp = df_filtered[WeatherFields.TEMPERATURE].median()
    temp_range = max_temp - min_temp

    st.write(f"**Temperature Statistics:**")
    st.write(f"- Average Temperature: {avg_temp:.2f} °C")
    st.write(f"- Minimum Temperature: {min_temp:.2f} °C")
    st.write(f"- Maximum Temperature: {max_temp:.2f} °C")
    st.write(f"- Standard Deviation: {std_temp:.2f} °C")
    st.write(f"- Median Temperature: {median_temp:.2f} °C")
    st.write(f"- Temperature Range: {temp_range:.2f} °C")