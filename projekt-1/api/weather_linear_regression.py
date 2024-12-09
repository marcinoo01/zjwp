import pandas as pd
from matplotlib import pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error
from .weather_enum import WeatherFields

class WeatherLinearRegression:
    def __init__(self, dataframe):
        self.df = dataframe

    def get_model(self):
        """
        Fits a linear regression model using temperature as predictor and feels-like as target.
        Returns the fitted model.
        """
        X = self.df[[WeatherFields.TEMPERATURE]]
        y = self.df[WeatherFields.FEELS_LIKE]

        model = LinearRegression()
        return model.fit(X, y)

    def calculate_model_statistics(self):
        """
        Calculates regression model statistics and returns an object containing all relevant metrics.
        """
        model = self.get_model()
        x = self.df[[WeatherFields.TEMPERATURE]]
        y = self.df[WeatherFields.FEELS_LIKE]
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

    def plot_model(self, stats):
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

