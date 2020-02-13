magicians = ['david', 'alice', 'carolina', 'danil', 'sasha', 'anya', 'dasha', 'galya']
for magician in magicians:
    print(magician.title() + ' очень классый фокусник!')
    print('Фокусника по именем ' + magician.title() + ' я не смотрел, но наверное стоит\n')
# Цикл for нужен для того чтобы перепрать все элементы списка и выполнить с каждым элементом одну и ту же операцию.
# В ситуациях, требующтх применение одного действия к каждому элементу списка, можно воспользоваться цикломи for.
print('Спасибо вам фокусники за хорошее выступление')

print('\nThe first three items in the list are:')
print(magicians[:3])
# Первое задание 4-10.
print('\nThree items from the middle of the list are:')
print(magicians[3:-2])
# Второе задание 4-10.
print('\nThe last three items in the list are:')
print(magicians[-3:])
# Третье задание 4-10.
