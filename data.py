import numpy as np

#table
dates = np.array([
    '2025-01-01', '2025-01-02', '2025-01-03', 
    '2025-01-04', '2025-01-05'
])


weather_data = np.array([
    [22, 65, 15, 2.5],
    [25, 70, 10, 0.0],
    [20, 60, 20, 5.0],
    [18, 55, 25, 12.0],
    [24, 75, 5, 0.0]
])

#questions

avg_temp = np.mean(weather_data[:, 0])
print("1.Average Temperature:", avg_temp)

max_humidity = np.max(weather_data[:, 1])
print("2.Maximum Humidity:", max_humidity)

max_wind_day = np.argmax(weather_data[:, 2])
print("3.Day with Maximum Wind Speed:", dates[max_wind_day])

total_rainfall = np.sum(weather_data[:, 3])
print("4.Total Rainfall:", total_rainfall)

hot_days = dates[weather_data[:, 0] > 22]
print("5.Days with Temperature Above 22°C:", hot_days)

humid_days_wind_speeds = weather_data[weather_data[:, 1] > 60][:, 2]
avg_wind_humid_days = np.mean(humid_days_wind_speeds)
print("6.Average Wind Speed on Humid Days:", avg_wind_humid_days)

max_rain_day = np.argmax(weather_data[:, 3])
print("7.Day with Highest Rainfall:", dates[max_rain_day])

temp_variance = np.var(weather_data[:, 0])
print("8.Variance in Temperature:", temp_variance)

humidity_std_dev = np.std(weather_data[:, 1])
print("9.Standard Deviation of Humidity:", humidity_std_dev)

windy_days_data = weather_data[weather_data[:, 2] > 10]
print("10.Data for Days with Wind Speed > 10 km/h:\n", windy_days_data)

rainfall = weather_data[:, 3]
normalized_rainfall = (rainfall - np.min(rainfall)) / (np.max(rainfall) - np.min(rainfall))
print("11.Rainfall Normalized to 0-1 Range:", normalized_rainfall)

correlation_temp_humidity = np.corrcoef(weather_data[:, 0], weather_data[:, 1])[0, 1]
print("12.Correlation Between Temperature and Humidity:", correlation_temp_humidity)

cumulative_rainfall = np.cumsum(weather_data[:, 3])
print("13.Cumulative Rainfall:", cumulative_rainfall)

calm_days = dates[weather_data[:, 2] < 10]
print("14.Calm Days (Wind Speed < 10 km/h):", calm_days)

no_rain_days = dates[weather_data[:, 3] == 0]
print("15.Days Without Rainfall:", no_rain_days)

