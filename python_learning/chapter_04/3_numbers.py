for red in range(1,6):
    print(red)
# Функция range() в цикле for упращает построение числовых последовательностей. С её помощю можно вывести серию чисел в столбик вписав в круглые скобки функции числа, которые надо вывести(range(1,6). Пример выше.
# Числа, выводятся со смещением на 1, по этому если программа выводит не тот результат, на который вы расчитывали, попробуйте увеличить конечное значение в скобках на 1.
numbers = list(range(1,6))
print(numbers)
# list(). Если нужно создать числовой список, нужно заключить вызов range() в list(), тогда результат будет представлять собой список с числовыми элементами.