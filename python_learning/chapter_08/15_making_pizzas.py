import pizza
pizza.make_pizza(16, 'pepperoni')
pizza.make_pizza(12, 'mushroms', 'green peppers', 'extra cheese')
# Команда import сообщает Python, что код модуля должен быть доступен в текущем выполняемом программном файле.

# В процессе обработки этого файла строка import pizza приказывает Python открыть файл pizza.py и скопировать все функции из него в программу.

"""Любая функция, определённая в pizza.py, будет доступна в making_pizzas.py"""

# Чтобы вызвать функцию из импортированного модуля, нужно указать имя модуля (pizza), точку и имя функции (making_pizzas()) 'шаблон'- имя_модуля.имя_функции().

# "Импортирование всего модуля" стр. 155-156.

from pizza import make_pizza

make_pizza(16, 'pepperoni')
make_pizza(12, 'mushroms', 'green peppers', 'extra cheese')
# Также возможно импортировать конкретную функцию из модуля. Общий синтаксис выглядит так: from имя_модуля import имя_функции.

# Можно импортировать любое количество функций из модуля, разделив их имена запятыми.

# При таком синтаксисе использовать точечную запись при вызове функции не обязательно.

# "Импортирование конкретных функций." стр.156-157.

from pizza import make_pizza as mp

mp(16, 'pepperoni')
mp(12, 'mushroms', 'green peppers', 'extra cheese')
# Чтобы заменить имя функции на псевдоним, нужно после оригинального названия функции ввести ключевое слово 'as' после которого следует новое имя для функции.

# Общий синтаксис выглядит так: from имя_модуля import имя_функции as псевдоним

# "Назначение псевдонима для функции" стр.156.

import pizza as p

p.make_pizza(16, 'pepperoni')
p.make_pizza(12, 'mushroms', 'green peppers', 'extra cheese')
# Чтобы заменить имя модуля на псевдоним, нужно после оригинального названия модуля ввести ключевое слово 'as' после которого следует новое имя для функции.

# Общий синтаксис выглядит так: import имя_модуля as псевдоним.

# "Назначение псевдонима для модуля" стр. 157.

from pizza import *

make_pizza(16, 'pepperoni')
make_pizza(12, 'mushroms', 'green peppers', 'extra cheese')
# Звёздочка в команде import приказывает Python скопировать каждую функцию из модуля pizza в файл программы.

# После импортирования всех функций можно вызывать каждую функцию по имени без точечной записи, но лучше не использовать этот способ.

# Синтаксис выглядит так: from имя_модуля import *

# "Импортирование всех функций модуля" стр. 157.
