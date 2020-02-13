for danil in range(1,21):
    print(danil)
#Считаем до 20.

for sad in range(1,10):
    print(sad)
# Миллион.
mouse = list(range(1,1000001))
print(min(mouse))
print(max(mouse))
print(sum(mouse))
# Суммирование миллиона.

for genius in range(1,21,2):
    print(genius)
# Нечётные числа.

for tone in list(range(3,31,3)):
    print(tone)
# Тройки.

for dogy in range(1,11):
    wow = dogy**3
    print(wow)
# Кубы.

cubes = [numbers**3 for numbers in range(1,11)]
print(cubes)
# Генератор кубов.
