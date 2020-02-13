import csv
import pygal

from datetime import datetime

filename = 'sitka_weather_2014.csv'
with open(filename) as f:
    reader = csv.reader(f)
    headers = next(reader)

    dates, highs, lows = [], [], []
    for row in reader:
        date = datetime.strptime(row[0], '%Y-%m-%d')
        high = int(row[1])
        low = int(row[3])

        dates.append(date)
        highs.append((date, high))
        lows.append((date, low))

ln = pygal.DateLine(x_label_rotation=20, fill=True)
ln.title = 'Weather of Sitka by 2014.'
ln.x_labels = [dates[i] for i in range(0, len(dates)+1, int(len(dates)/5))]

ln.add('Max temperatures', highs)
ln.add('Min temperatures', lows)

ln.render_to_file('weather_sitka_pygal.svg')