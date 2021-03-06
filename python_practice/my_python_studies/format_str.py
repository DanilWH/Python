text = 'Hello, {name}!'.format(name='Danil')
print(text)

text = "Name: {name}\t Age: {name}'у '{age} лет\n".format(name='Danil', age=16)
print(text)
# Примеры форматирования именованных параметров.

info = "Name: {0}\t Age: {1}\n".format('Danil', 16)
print(info)
# Пример форматирования параметров по позиции.

string = "name: {}\t age: {}".format('Danil', 16)
print(string)
# Пример форматирования последовательных параметров. То есть первый параметр в
# собках будет в превых фигурных скобках, которые соделжатся в строке, второй
# параметр за вторые скобки. То есть они идут последовательно.
# (Этого в телефонном приложении нет)

# Ниже примеры форматирования методом подстановки плейсхолдеров:
# s: для вставки строк.
# d: для вставки целых чисел.
# f: для вставки дробных чисел.
# %: умнодает значение на 100 и добавляет знак процента.
# e: выводит число в экспанециальной записи.
# для плейсхолдеров s, d, f, %, e можно определять через точку количество
# знаков в дробной части, а по необходимости перед этим задавать количество
# символов перед форматируемым числом.
# Общее формальное определение форматирования чисел выглядит так:
# {:[количество_символов][запятая].[число_знаков_в_дробной_части] плейсхолдер}
welcome = "Hello, {:s}!\n".format('Danil')
print(welcome)

sourse = "{:,d} symbols.\n".format(2000000)
print(sourse)

number = "{:10.3f}".format(2449.233457837234)
print(number)
number = "{:6d}\n".format(2449)
print(number)

procent = 0.634
print("{:.1%}\n".format(procent))

number = 1234.5678
print("{:e}".format(number))
print("{:.0e}".format(number))
print("{:.1e}\n".format(number))

# ФОРМОТИРОВАНИЕ БЕЗ МЕТОДА FORMAT.
# Мы можем обойтись и без метода format, применяя следующий синтаксис:
# строка%(параметр1, параметр2,..прараметрN)
# Тоесть в начале идёт строка, которая содердит те же плейсхолдеры(за
# исключением %) после строки ставится знак процента, а затем список знасений,
# которые вставляются в строку.
info = "Name: %s \t Age: %d\n" %('Danil', 16)
print(info)

number = 234.67438
print("%,0.2f = %e" %(number, number))
