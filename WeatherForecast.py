import openmeteo_requests
import pandas as pd
import requests_cache
from retry_requests import retry
from zoneinfo import ZoneInfo

# Setup the Open-Meteo API client with cache and retry on error
cache_session = requests_cache.CachedSession('.cache', expire_after=3600)
retry_session = retry(cache_session, retries=5, backoff_factor=0.2)
openmeteo = openmeteo_requests.Client(session=retry_session)

# Define API URL and parameters
url = "https://api.open-meteo.com/v1/forecast"
params = {
    "latitude": 39.174144,
    "longitude": -86.520627,
    "daily": ["temperature_2m_max", "temperature_2m_min", "sunset", "precipitation_probability_max"],
    "forecast_days": 1,
    "wind_speed_unit": "ms"
}

# Send the request
responses = openmeteo.weather_api(url, params=params)

# Process the first location
response = responses[0]
print(f"Elevation: {response.Elevation()} m Above Sea Level")

# Process daily data
daily = response.Daily()
daily_temperature_2m_max = daily.Variables(0).ValuesAsNumpy()
daily_temperature_2m_min = daily.Variables(1).ValuesAsNumpy()
daily_sunset = daily.Variables(2).ValuesInt64AsNumpy()
daily_precipitation_probability_max = daily.Variables(3).ValuesAsNumpy()

# Generate date range from API timestamps
daily_dates = pd.date_range(
    start=pd.to_datetime(daily.Time(), unit="s", utc=True),
    end=pd.to_datetime(daily.TimeEnd(), unit="s", utc=True),
    freq=pd.Timedelta(seconds=daily.Interval()),
    inclusive="left"
)

# Define Indiana timezone
indiana_tz = ZoneInfo("America/Indiana/Indianapolis")

# Convert first date and sunset time to Indiana local time
forecast_date_local = daily_dates[0].astimezone(indiana_tz).strftime("%Y-%m-%d")
sunset_time_local = pd.to_datetime(daily_sunset[0], unit="s", utc=True).astimezone(indiana_tz).strftime("%H:%M")

# Assign each weather variable to a Python variable
temperature_2m_max = daily_temperature_2m_max[0]
temperature_2m_min = daily_temperature_2m_min[0]
precipitation_probability_max = daily_precipitation_probability_max[0]

print(f"Forecast Date (IN): {forecast_date_local}")
print(f"Max Temp: {temperature_2m_max:.2f} °C")
print(f"Min Temp: {temperature_2m_min:.2f} °C")
print(f"Sunset Time (IN): {sunset_time_local}")
print(f"Max Precipitation Probability: {precipitation_probability_max:.2f} %")

