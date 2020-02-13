import csv
import matplotlib.pyplot as plt

from datetime import datetime

def get_wind(filename, dates, max_wind):
    with open(filename) as file_object:
        reader = csv.reader(file_object)
        headers = next(reader)

        for curr_data in reader:
            try:
                date = datetime.strptime(curr_data[0], '%Y-%m-%d')
                wind = int(curr_data[16])
            except ValueError:
                print(f'By {date} no data.')
            else:
                dates.append(date)
                max_wind.append(wind)
# Getting of screen figure.
fig = plt.figure()

# Sublumt of graph.
filename = 'data/death_valley_2014.csv'
dates, max_wind = [], []
get_wind(filename, dates, max_wind)
plt.plot(dates, max_wind, c='blue', alpha=0.5)
plt.fill_between(dates, max_wind, facecolor='black', alpha=0.1)

# Format graph.
plt.title("Wind speed by 2014, Death Valley", fontsize=24)
plt.xlabel("Dates", fontsize=14)
plt.ylabel("Speed (MPH)", fontsize=14)
plt.tick_params(axis='both', labelsize=12)
fig.autofmt_xdate()
plt.axis([min(dates), max(dates), 0, max(max_wind)*1.05])

plt.show()