my_pizzas = ['marinara', 'margaritta', 'carbonara', 'beluchi', 'bovaria']
for pizzas in my_pizzas:
    print('I like pizza ' + pizzas.title() + '!')
print('Thanks to the Italian for creating such dishes as pizza! BRAVO!!!')
# Это задание 4-1 про пиццы.

animals = ['raccoon' , 'bear', 'bird', 'man', 'snacke']
print('')
for animals in animals:
    print(animals.title() + '-very funny animal.')
print('\nThese animals are so funny)))')
# Это задание 4-2 про животных.

freind_pizzas = my_pizzas[:]

my_pizzas.append('vegetable')
freind_pizzas.append('dill')

print('\nMy favorile pizzas are:')
for my_pizza in my_pizzas:
    print(my_pizza.title())
    # Моя пицца
print("\nMy frend's favorite pizzas are:")
for freind_pizza in freind_pizzas:
    print(freind_pizza.title())
    # Пицца друга
# Начиная с freind_pizzas = my_pizzas[:], это было практическое задание 4-11 про пиццы.
