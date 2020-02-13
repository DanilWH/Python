import sixteen_homework_functions

name_magicans_list = ['fas', 'gas', 'ter', 'oga', 'nas']
name_magicans_great = []
sixteen_homework_functions.show_magicans(name_magicans_list)
sixteen_homework_functions.make_great(name_magicans_list[:])# Использовал копирование чтобы работал следующий способ.
# 1 задание упражнения 8-16.

print(" ")

from sixteen_homework_functions import make_great

make_great(name_magicans_list[:])# так же использовал копирование чтобы работал следующий способ.
# 2 задание упражнения 8-16.

print(" ")

from sixteen_homework_functions import make_great as mg

mg(name_magicans_list[:])# так же использовал копирование чтобы работал следующий способ.
# 3 задание упражнения 8-16.

print(" ")

import sixteen_homework_functions as shf

shf.make_great(name_magicans_list[:])# так же использовал копирование чтобы работал следующий способ.
# 4 задание упражнения 8-16.

print(" ")

from sixteen_homework_functions import *

show_magicans(name_magicans_list)
make_great(name_magicans_list)# Не использую копию списка так как этот способ является последним в этой программе и копирование безсмысленно.
# 5 задание упражнения 8-16.
