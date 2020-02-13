def make_shirt(size, text):
	print("Size shirt-" + size + ". Text shirt '" + text + "'.")

make_shirt('XL', 'I am program;-)')
make_shirt(text='I am program;-)', size='XL')
# Упражнение 8-3.

def make_shirt(text, size='L'):
	print("Size shirt-" + size + ". Text shirt '" + text + "'.")

make_shirt(text='I love Pythot.')
# 1 задание в упражнении 8-4.

def make_shirt(size='L', text='I love Python.'):
	print("Size shirt-" + size + ". Text shirt '" + text + "'.")

make_shirt()
make_shirt(size='XXL', text='I love Los-Angeles.')
# Упражнение 8-4.

def describe_city(city, country='USE'):
	print(city + " in " + country + ".")

describe_city(city='Los-Angeles')
describe_city(city='Moskow', country='Russia')
describe_city(city='San-Francisko')
# Упражнение 8-5.
