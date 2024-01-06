# Temperature Blanket Tool

This tool helps you design and plan a knitted or crocheted temperature blanket by calculating and prototyping color choices based on historical temperature data. 

## Getting the temperature history for your location 
Visit https://www.weatherapi.com/ and create a free account.

Copy your API Key for WeatherAPI.

In `request_weather.py`, set your location and date range. Currently using the daily average, but consider highs and lows. 

Run `request_weather.py` to generate a CSV file: weather_info_{location}.csv.

Example CSV Output:

```
date,avg_temperatures_f,avg_temperatures_c
2023-01-04,53.9,12.2
2023-01-05,52.8,11.6
2023-01-06,48.4,9.1
2023-01-07,50.7,10.4
```

## Mapping colors to temperature ranges 

In `mapping_colors.py`, set the 10 yarn colors you plan to use. Adjust this depending on the number of yarn colors.

Run `mapping_colors.py`, to see the temperature-color mapping.

Example colors:

![Alt text](colors.png)

Based on the input of the previous years temperature, this is how London 2023 would look: 
![Alt text](daily_London_avg_temperatures_c.png)

You will then get the following output, which you can apply to your upcoming year.
```
darkblue: 	   	-0.2
blue: 	        	2.44
lightblue:  		5.08
teal: 	        	7.72
lightgreen: 		10.36
greenyellow: 		13.0
yellow: 	    	15.64
orange: 	    	18.28
darkorange: 		20.92
brightred: 	    	23.56
```
