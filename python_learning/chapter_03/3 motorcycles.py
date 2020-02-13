motorcycles = ["kozol", "yamaha", "honda", "suzuki"]
print(motorcycles)

motorcycles[0] = "kavasaki"
print(motorcycles)
# Чтобы изменить элемент в списке нужно к имени списка (переменной) приписать номер элемента списка и заменить его на новый.

motorcycles = ["kozol", "yamaha", "honda", "suzuki"]
print(motorcycles)

motorcycles.append("kavasaki")
print(motorcycles)
# append()-Чтобы добавить новый элемент в конец списка (это является самый лёгкий способ) нужно к имени списка (переменной) присвоить метод append() и в скобки вписать строку нового элемента.

motorcycles = []

motorcycles.append("kozol")
motorcycles.append("yamaha")
motorcycles.append("honda")
motorcycles.append("suzuki")
print(motorcycles)
# Чтобы пользователь программы мог управлять содержимым списка, лучше начать определение с пустого списка, а затем присоединять к нему каждое значение.

motorcycles = ["kozol", "yamaha", "honda", "suzuki"]

motorcycles.insert(0, "kavasaki")
print(motorcycles)
# Метод insert() позволяет добавить новый элемент в произвольную позицию списка. Для этого стоит указать индекс(место в списке) и значение нового элемента в скобки.

motorcycles = ["kozol", "yamaha", "honda", "suzuki"]
print(motorcycles)

del motorcycles[1]
print(motorcycles)
# Комаеда del позволяет удалить элемент из любой позиции списка, если вам известен его индекс.

motorcycles = ["kozol", "yamaha", "honda", "suzuki"]
print(motorcycles)

popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)
# Метод pop() удаляет элемент из списка, но позволяет работать с ним после удаления.
# pop() используется тогда, когда знаешь позицию элемента, которого нужно удалить из списка.
# Пример где это может  использоваться:
motorcycles = ["kozol", "yamaha", "honda", "suzuki"]

purchased_motorcycles = motorcycles.pop(-2)# Чтобы удалить элемент в произвольной позиции списка; для этого следует указать индекс удаляемого в круглых скобках.
message = "К вашему сожалению, мотоцикл " + purchased_motorcycles.title() + " уже купили!"
print(message)
# "Если вы собираетесь просто удалить элемент из списка, никак не используя его, выбирайте команду del; если же вы намерены использовать элемент после удаления из списка, выбирайте метод pop()."

motorcycles = ["kozol", "yamaha", "honda", "suzuki"]
print(motorcycles)

new = "yamaha"
motorcycles.remove(new)
print(motorcycles)
message = new.title() + " офигенный мотоцикл!"
print(message)
# remove() "Если вы знаеете только значение элемента. используйте метод remove() (в круглых скобках пишем значение элемента).
# Метод remove() также может использоваться для работы со значением, которое удаляется со списка.
