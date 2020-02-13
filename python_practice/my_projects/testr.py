import random
import pyttsx3

actions = ['+', '-', '*', '/']
a = random.randint(0, 100)
b = random.randint(0, 100)
action = random.sample(actions, 1)[0]

if action == '+':
	result = (a + b)
elif action == '-':
	result = (a - b)
elif action == '*':
	result = (a * b)
elif action == '/':
	try:
		result = (a / b)
	except ZeroDivisionError:
		result = (" You can't divide by 0!")
	else:
		result = result

print(str(a) + str(action) + str(b))
print(result)
# Механизм калькулятора.

engine = pyttsx3.init()

engine.say(str(a) + str(action) + str(b))
engine.say(result)
engine.runAndWait()
# Речь калькулятора.
