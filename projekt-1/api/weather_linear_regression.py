from matplotlib import pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error
from .weather_enum import WeatherFields
from .weather_data_presenter import display_model_statistics

def calculate_model_statistics(df):
    """
    Calculates regression model statistics and returns an object containing all relevant metrics.
    """
    x = df[[WeatherFields.FEELS_LIKE]]
    y = df[WeatherFields.TEMPERATURE]
    model = LinearRegression()
    model.fit(x, y)

    stats = type('ModelStats', (object,), {})()

    stats.coefficient = model.coef_[0]
    stats.intercept = model.intercept_
    stats.r_squared = model.score(x, y)
    predictions = model.predict(x)

    stats.mae = mean_absolute_error(y, predictions)
    stats.mse = mean_squared_error(y, predictions)
    stats.rmse = stats.mse ** 0.5
    residuals = y - predictions
    stats.rss = sum(residuals ** 2)
    stats.predictions = predictions
    stats.X = x
    stats.y = y

    return stats


def plot_model(stats):
    """
    Generates a scatter plot of actual vs predicted values and the regression line.
    """
    fig, ax = plt.subplots()
    ax.scatter(stats.X, stats.y, color="blue", label="Actual (feels_like)")
    ax.plot(stats.X, stats.predictions, color="red", label="Predicted (feels_like)")
    ax.set_xlabel("Feels-like (°C)")
    ax.set_ylabel("Temperature (°C)")
    ax.set_title("Regression: Temperature vs Feels-like")
    ax.legend()
    return fig


def perform_linear_regression(filtered_df, st):
    if len(filtered_df) > 1:
        model_stats = calculate_model_statistics(filtered_df)
        display_model_statistics(model_stats, st)
        fig = plot_model(model_stats)
        st.pyplot(fig)
    else:
        st.write("Not enough data for analysis.")
