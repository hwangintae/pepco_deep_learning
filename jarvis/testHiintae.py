import speech_recognition as sr
import os
from gtts import gTTS

def listen():
	r = sr.Recognizer()
	with sr.Microphone() as source:
		a = r.listen(source)

	try:
		r = r.recognize_google(a)
		print(r)

	except sr.UnknownValueError:
		print("could not understand audio")

	except sr.RequestError as e:
		print("recog error".format(e))

	tts = gTTS(r, lang = 'en')
	tts.save("save.mp3")
	if r == "hi" :
		os.system("hiInTae.mp3")
	else :
		os.system("save.mp3")

	return ""

listen()