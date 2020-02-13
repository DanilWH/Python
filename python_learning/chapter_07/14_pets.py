pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)

while 'cat' in pets:
	pets.remove('cat')

print(pets)
# Чтобы удалить из списка все экземпляры 'cat', нужно в цикле while к имени списа применить метод remove() и в круглые скобки вписать что нужно удалить.
