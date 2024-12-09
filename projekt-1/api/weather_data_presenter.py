class WeatherPresenter:
    @staticmethod
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

    @staticmethod
    def display_weather_statistics(stats, st):
        """
        Displays the general weather statistics using Streamlit.
        """
        st.write(f"- **Average Temperature**: {stats.avg_temp:.2f}°C")
        st.write(f"- **Average Feels-like Temperature**: {stats.avg_feels_like:.2f}°C")
        st.write(f"- **Maximum Temperature**: {stats.max_temp}°C ({stats.hottest_location} on {stats.hottest_date})")
        st.write(f"- **Minimum Temperature**: {stats.min_temp}°C ({stats.coldest_location} on {stats.coldest_date})")
