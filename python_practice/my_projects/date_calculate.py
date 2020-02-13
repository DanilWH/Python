from datetime import timedelta, datetime

now = datetime.today()
year = 2002
month = 10
day = 6
date_of_birth = datetime(year, month, day)

period = now - date_of_birth

#year = period.year
#total_months = period.month
total_days = period.days
total_seconds = period.total_seconds()
total_microseconds = period.microseconds
print('Всего:\n{} дней;\n{} секунд;\n{} микросекунд'.format(
    total_days, round(total_seconds, 1), round(total_microseconds, 1)))
