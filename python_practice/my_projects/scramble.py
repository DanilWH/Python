import random

def check_number_back_elements(back_element, choice_element):
	if len(back_element) > 1:
		del back_element[0]
	back_element.append(choice_element)

def get_format_elements(choice_element, ready_elements_for_scramble,
		back_element, speck_element=''):
	format_element = choice_element + speck_element
	ready_elements_for_scramble.append(format_element)
	check_number_back_elements(back_element, choice_element)

scramble_elements = ['U', 'R', 'B', 'L', 'F', 'D']
ready_elements_for_scramble = []

back_element = []
number = 0

users_number_scramble = input("How many steps do you want to do?: ")
number_steps = int(users_number_scramble)

while number < number_steps:

	a = random.randint(0, 5)
	choice_element = scramble_elements[a]
	if choice_element in back_element:
		continue
	else:
		number += 1
		b = random.randint(0, 2)
		if b == 1:
			get_format_elements(choice_element, ready_elements_for_scramble,
				back_element, speck_element="'")
		elif b == 2:
			get_format_elements(choice_element, ready_elements_for_scramble,
				back_element, speck_element='2')
		else:
			ready_elements_for_scramble.append(choice_element)
			check_number_back_elements(back_element, choice_element)

print(' '.join(ready_elements_for_scramble))
print(len(ready_elements_for_scramble))
