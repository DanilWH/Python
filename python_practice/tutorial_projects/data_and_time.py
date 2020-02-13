import datetime

now = datetime.datetime.now()

print()
print("Текущая дата и время с использованием метода str:")
print(str(now))

print()
print("Текущая дата и время с использованием атрибутов:")
print("Текущий год: %d" % now.year)
print("Текущий месяц: %d"% now.month)
print("Текущий день: %d" % now.day)
print("Текущий час: %d" % now.hour)
print("Текущая минута: %d" % now.minute)
print("Текущая секунда: %d" % now.second)
print("Текущая микросекунда: %d" % now.microsecond)

print()
print("Текущая дата и время с использованием strftime:")
print(now.strftime("%d-%m-%Y %H:%M"))

print()
print("Текущая дата и время с использованием isoformat:")
print(now.isoformat())
"""
Другие полезные методы класса datetime:
datetime.today() - текущая дата, время равно 0.

datetime.fromtimestamp(timestamp) - дата из стандартного представления времени.

datetime.date() - объект даты (с отсечением времени).

datetime.time() - объект времени (с отсечением даты).

datetime.combine(date, time) - объект datetime из комбинации объектов date и time.

datetime.replace([year[, month[, day[, hour[, minute[, second[, microsecond[, tzinfo]]]]]]]]) - возвращает новый объект datetime с изменёнными атрибутами.

datetime.weekday() - день недели в числовом формате, понедельник - 0, воскресенье - 6.

datetime.isoweekday() - день недели в числовом формате, понедельник - 1, воскресенье - 7.

datetime.strptime(date_string, format) - преобразует строку в datetime.

datetime.strftime(format) - преобразует datetime в строку в datetime.
"""
