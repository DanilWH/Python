import csv

from matplotlib import pyplot as plt
from datetime import datetime

# Reading data from file.
filename = 'data/sitka_weather_2014.csv'
with open(filename) as f:
    read_obj = csv.reader(f)
    headers = next(read_obj)

    dates, rains = [], []
    for rain_data in read_obj:
        try:
            date = datetime.strptime(rain_data[0], '%Y-%m-%d')
            curr_rainfall = float(rain_data[19])
        except ValueError:
            print(f'{date} missing data')
        else:
            dates.append(date)
            rains.append(curr_rainfall)

# Sumlimt of graph.
fig = plt.figure()
plt.plot(dates, rains, c='blue', alpha=0.5)
plt.fill_between(dates, rains, facecolor='blue', alpha=0.1)

# Formating of graph.
plt.title("Data of rainfall by 2014, Sitka", fontsize=24)
plt.xlabel("Date", fontsize=14)
plt.ylabel("Number of rainfall", fontsize=14)
plt.ylim(0, max(rains)*1.05)
fig.autofmt_xdate()

plt.show()