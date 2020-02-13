import pyttsx3
engine = pyttsx3.init()

engine.say("hi this is test voice")

engine.runAndWait()
# Это простая версия синтезатора речи.

def output(x):
    engine = pyttsx3.init()
    rate = engine.getProperty('rate')
    engine.setProperty('rate', rate-70)
    print("Pc: "+x+".")
    engine.say(x)
    engine.runAndWait()
output("hi this is test voice")
# Эта версия позволяет настраивать скорость воспроизведения речи.

__Author = "Pythoners"
y = pyttsx3.init()
y.setProperty("rate", 115)
x = str(input("What do you want to say?"))
y.say(x)
y.runAndWait()

y = pyttsx3.init()
voice = y.getProperty('voices')
for x in voice:
	y.setProperty('voice', x.id)
	y.say("Hello world,can you hear us, hello again i hope you can hear this")
	y.runAndWait()
# Другие варианты воспроизведения речи.