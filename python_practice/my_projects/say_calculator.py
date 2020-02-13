import pyttsx3
import sys

engine = pyttsx3.init()

def programm():
	message = "\nEnter 'OFF' to exit;"

	while True:
		print(message)
		engine.say("Enter furst number value.")
		engine.runAndWait()
		first = input("Enter furst number value: ")
		if first == 'off':
			engine.say("Exit")
			engine.runAndWait()
			break
		elif first != 'off':
			engine.say(first)
			engine.runAndWait()

		print(message)
		engine.say("Enter event value.")
		engine.runAndWait()
		event = input("Enter event value: ")
		if event == 'off':
			engine.say("Exit")
			engine.runAndWait()
			break
		elif event != 'off':
			engine.say(event)
			engine.runAndWait()

		print(message)
		engine.say("Enter last number value.")
		engine.runAndWait()
		last = input("Enter last number value: ")
		if last == 'off':
			engine.say("Exit")
			engine.runAndWait()
			break
		elif last != 'off':
			engine.say(last)
			engine.runAndWait()

		if event == '+':
			result = (int(first) + int(last))
		elif event == '-':
			result = (int(first) - int(last))
		elif event == '*':
			result = (int(first) * int(last))
		elif event == '/':
			try:
				result = (int(first) / int(last))
			except ZeroDivisionError:
				result = ("You can't divide by 0!")
				engine.say("You can't divide by 0! ")
				engine.runAndWait()
			else:
				result = result

		print(str(first) + str(event) + str(last))
		print("Answer: " + str(result))

		engine.say(str(first) + str(event) + str(last))
		engine.say("Answer: " + str(result))
		engine.runAndWait()

while programm:
	engine.say('Enter "ON" or "OFF" to enable calculator.')
	engine.runAndWait()

	switch = ''
	while switch.lower() != 'on':
		switch = input('Enter "ON", "OFF" or "END" to enable, turn off or end session calculator: ')
		if switch.lower() == 'end':
			engine.say("END")
			engine.runAndWait()
			sys.exit()
	programm()
