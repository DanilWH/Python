from gtts import gTTS
import os    

tts = gTTS(text="Жалко", lang='ru')
tts.save("pcvoice.mp3")
# to start the file from python
os.system("start pcvoice.mp3")