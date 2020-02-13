"""Temperature of San-Francisco is close to Death Valley!"""

import csv

from datetime import datetime
from matplotlib import pyplot as plt

filename = 'data/TSan-Francisco.csv'
with open(filename) as f:
    reader_object = csv.reader(f)
    headers = next(reader_object)
    
    dates, highs, lows = [], [], []
    for row in reader_object:
        try:
            curr_date = datetime.strptime(row[2], '%Y-%m-%d')
            high = int(row[4])
            low = int(row[5])
        except ValueError:
            print(f'{curr_date} missing data.')
        else:
            dates.append(curr_date)
            highs.append(high)
            lows.append(low)

# sublimt the graph.
fig = plt.figure()
plt.plot(dates, highs, c='red', alpha=0.5)
plt.plot(dates, lows, c='blue', alpha=0.5)

# Format the garph.
plt.tick_params(axis='both', labelsize=14)
fig.autofmt_xdate()
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

plt.show()