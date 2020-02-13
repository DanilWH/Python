world_list = ["автострада", "бензин", "инопланетянин",\
              "самолет", "библиотека", "шайба", "олимпиада"]
print(world_list)
print(world_list[2].title())
print(world_list[-3].title())

message = "Hello " + world_list[2].title() + ", how are you?"
print(message)

world_list[-2] = "часы"
print(world_list)

world_list.append("футболка")
print(world_list)

world_list.append("автомобиль")
world_list.append("python")
world_list.append("вентилятор")
print(world_list)

world_list.insert(3, "утюг")
world_list.insert(5, "говно")
print(world_list)

del world_list[5]
print(world_list)

new = world_list.pop(-6)
print(world_list)
print("У меня дома " + new + " висят.")
del new

rutina = world_list.pop()
print(world_list)
print(rutina)
# pop() удаляет последний элемент списка, pop(-6) удаляет 7 элемент списка, он может использоваться для удаления элемента в произвольной позиции.
# pop() удаляет элемент из списка но сохраняет его в переменной где выполняется действие с pop(). С удалённым элементом в дальнейшем ещё можно будет работать.
world_list.remove("библиотека")
print(world_list)
# remove() используется для того, если не знаеш значение элемента. В круглые скобки нужно вписаль название элемента из списка.
yo = "утюг"
world_list.remove("утюг")
print(world_list)
print(yo)
print("У моей мамы дома имеется " + yo + ".")
# remove() так же может удалять элемент из списка и сохранять удалённый элемент списка с которым ещё можно будет в дальнейшем работать(пример как это делать показан выше).

print("\nNot sorted")
print(world_list)

print("\nWich sorted")
print(sorted(world_list))

print("\nWich sorted(back up)")
print(sorted(world_list, reverse=True))

print("\nNot sorted again")
print(world_list)
# Временная сортировка.

world_list.reverse()
print(world_list)
# reverse() просто переворачивает элементы списка "задом на перёд", но не в алфавитном порядке
world_list.reverse()
print(world_list)
# Повторное приминение reverse() возвращает элементы списка к исходному порядку.

world_list.sort()
print(world_list)
# sort() сортирует в алфавитном порядке, но вернуться к исходному порядку элементов списка уже не удастся.
world_list.sort(reverse=True)
print(world_list)
# sort(reverse=True) сортирует в обратном алфавитном порядке, но так же вернуться к исходному порядку элементов списка, уже невозможно.
print(len(world_list))
print("Количество элементов в списке:" + str(len(world_list)))
