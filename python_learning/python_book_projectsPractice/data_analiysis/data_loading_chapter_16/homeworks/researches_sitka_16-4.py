import csv

from matplotlib import pyplot as plt
from datetime import datetime

def get_humidity(filename, dates, max_humidity, min_humidity):
    with open(filename) as f:
        reader_obj = csv.reader(f)
        headers = next(reader_obj)

        for string in reader_obj:
            try:
                date = datetime.strptime(string[0], '%Y-%m-%d')
                max_hum = int(string[7])
                min_hum = int(string[9])
            except ValueError:
                print(f'{date} missing data')
            else:
                dates.append(date)
                max_humidity.append(max_hum)
                min_humidity.append(min_hum)
# getting a figure of screen.
fig = plt.figure()

# Sublimt the graph.
filename = 'data/sitka_weather_2014.csv'
dates, max_humidity, min_humidity = [], [], []
get_humidity(filename, dates, max_humidity, min_humidity)
plt.plot(dates, max_humidity, c='blue', alpha=0.6)
plt.plot(dates, min_humidity, c=(0.778, 0.763, 0.015), alpha=0.6)
plt.fill_between(dates, max_humidity, min_humidity, facecolor='blue',
    alpha=0.1)

# Format of graph.
plt.title("Humidity of Sitka by 2014", fontsize=24)
plt.xlabel("Dates", fontsize=14)
plt.ylabel("Humidity (%)", fontsize=14)
plt.tick_params(axis='both', labelsize=12)
fig.autofmt_xdate()

plt.show()