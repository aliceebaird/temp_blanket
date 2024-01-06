import requests
import datetime
from statistics import median
import os
import pandas as pd

# Function to fetch and process weather data
def fetch_weather_data(api_key, location, date):
    base_url = "http://api.weatherapi.com/v1/history.json"
    request_url = f"{base_url}?key={api_key}&q={location}&dt={date}"
    response = requests.get(request_url)
    if response.status_code == 200:
        data = response.json()
        avg_temp_f = data["forecast"]["forecastday"][0]["day"]["avgtemp_f"]
        avg_temp_c = data["forecast"]["forecastday"][0]["day"]["avgtemp_c"]
        return avg_temp_f, avg_temp_c
    else:
        print(f"Failed to retrieve data for {date}")
        return None, None

# Main script logic
def main():
    api_key = os.getenv("WEATHER_API_KEY")
    location = "London"  # US Zip, worldwide city

    current_date = datetime.date.today()
    date_str = current_date.strftime("%Y-%m-%d")

    avg_temp_f, avg_temp_c = fetch_weather_data(api_key, location, date_str)

    if avg_temp_f is not None and avg_temp_c is not None:
        weather_dict = {
            "date": [date_str],
            "avg_temperatures_f": [avg_temp_f],
            "avg_temperatures_c": [avg_temp_c],
        }

        df = pd.DataFrame.from_dict(weather_dict)
        filename = f"weather_info_{location}.csv"

        # Check if the file exists to determine append or write mode
        if os.path.exists(filename):
            df.to_csv(filename, mode='a', header=False, index=False)
        else:
            df.to_csv(filename, index=False)

if __name__ == "__main__":
    main()
