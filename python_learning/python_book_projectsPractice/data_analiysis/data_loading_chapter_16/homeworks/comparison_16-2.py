import csv

from datetime import datetime
from matplotlib import pyplot as plt

#plt.style.use('seaborn') # Используется из второго издания.

# Чтение дат и температурниых максимумов и минимумов Долины Смерти из файла.

def get_data(filename, dates, highs, lows):
    with open(filename) as f:
        reader = csv.reader(f)
        header_row = next(reader)

        for row in reader:
            try:
                current_date = datetime.strptime(row[0], '%Y-%m-%d')
                high = int(row[1])
                low = int(row[3])
            except:
                print(f'{current_date} missing data.')
            else:
                dates.append(current_date)
                highs.append(high)
                lows.append(low)

# Получение объекта фигуры для экрана.
fig = plt.figure(dpi=128, figsize=(10, 6))

filename = 'data/death_valley_2014.csv'
dates, highs, lows = [], [], []
get_data(filename, dates, highs, lows) # чтение данных Долины Смерти из файла.

# Нанесение данных на диаграмму для Долины Смерти.
plt.plot(dates, highs, c='red', alpha=0.2)
plt.plot(dates, lows, c='blue', alpha=0.2)
plt.fill_between(dates, highs, lows, facecolor='blue',
    alpha=0.05)

filename = 'data/sitka_weather_2014.csv'
dates, highs, lows = [], [], []
get_data(filename, dates, highs, lows) # чтение данных города Ситка из файла.

# Нанесение данных на диаграмму для города Ситка.
plt.plot(dates, highs, c='red')
plt.plot(dates, lows, c='blue')
plt.fill_between(dates, highs, lows, facecolor='blue',
    alpha=0.1)

# Форматирование диаграммы.
title = "Daily high and low temperatures - 2014\nDeath Valley and Sitka, USA"
plt.title(title, fontsize=20)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Temperature (F)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()