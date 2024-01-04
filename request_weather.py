import requests
import datetime
from statistics import median
import os 
import pandas as pd 

api_key = os.getenv('WEATHER_API_KEY')
location = 'London' # US Zip, worldwide city
base_url = 'http://api.weatherapi.com/v1/history.json'

start_date = datetime.date(2023, 1, 4) # YYYY, M, D
end_date = datetime.date(2024, 1, 4) 
# free calls only for the last year from current date
current_date = start_date

avg_temperatures_f = []
avg_temperatures_c = []
date_list = []
while current_date <= end_date:
    date_str = current_date.strftime('%Y-%m-%d')
    
    request_url = f'{base_url}?key={api_key}&q={location}&dt={date_str}'
    # print(request_url)
    response = requests.get(request_url)
    if response.status_code == 200:
        data = response.json()
        avg_temp = data['forecast']['forecastday'][0]['day']['avgtemp_f']

        avg_temp_c = data['forecast']['forecastday'][0]['day']['avgtemp_c']

        avg_temperatures_f.append(avg_temp)
        avg_temperatures_c.append(avg_temp_c)
        date_list.append(date_str)

        print(date_str, avg_temp)
    else:
        print(f'Failed to retrieve data for {date_str}')
    
    # Move to the next day
    current_date += datetime.timedelta(days=1)

median_temperature = median(avg_temperatures_f)
print(f'Median Temperature: {median_temperature}°F')

weather_dict = {'date': date_list,
                'avg_temperatures_f': avg_temperatures_f, 
                'avg_temperatures_c': avg_temperatures_c}

df = pd.DataFrame.from_dict(weather_dict)

df.to_csv(f"weather_info_{location}.csv", index=False)





