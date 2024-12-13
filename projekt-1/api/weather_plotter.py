from matplotlib import pyplot as plt
from .weather_enum import WeatherFields
import matplotlib.dates as mdates

def plot_model(stats):
    """
    Generates a scatter plot of actual vs predicted values and the regression line.
    """
    fig, ax = plt.subplots()
    ax.scatter(stats.X, stats.y, color="blue", label="Actual (feels_like)")
    ax.plot(stats.X, stats.predictions, color="red", label="Predicted (feels_like)")
    ax.set_xlabel("Temperature (°C)")
    ax.set_ylabel("Feels-like (°C)")
    ax.set_title("Regression: Feels-like vs Temperature")
    ax.legend()
    return fig

def plot_wind_vs_temp(st, df_filtered):
    plt.figure()
    plt.scatter(df_filtered[WeatherFields.TEMPERATURE], df_filtered[WeatherFields.WIND_SPEED], alpha=0.7)
    plt.xlabel("Temperature (°C)")
    plt.ylabel("Wind Speed (km/h)")
    plt.title("Wind Speed vs Temperature")
    st.pyplot(plt)

def plot_temp_vs_time(st, df_filtered):
    plt.figure()
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d %H:%M'))
    plt.gca().xaxis.set_major_locator(mdates.AutoDateLocator())
    plt.plot(df_filtered[WeatherFields.LOCALTIME], df_filtered[WeatherFields.TEMPERATURE], marker='o', linestyle='-')
    plt.gcf().autofmt_xdate()
    plt.xlabel("Date and Time")
    plt.ylabel("Temperature (°C)")
    plt.title("Temperature Trend")
    st.pyplot(plt)