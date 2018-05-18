import speech_recognition as sr
import pyttsx3
from gtts import gTTS

engine = pyttsx3.init()
engine.setProperty('rate', 140)

def speak(text) :
	engine.say(text)
	engine.runAndWait()

def listen():
	r = sr.Recognizer()
	with sr.Microphone() as source:
		audio = r.listen(source)

	try:
		r = r.recognize_google(audio)
		print(r)

	except sr.UnknownValueError:
		print("could not understand audio")

	except sr.RequestError as e:
		print("recog error".format(e))

	tts = gTTS(r, lang = 'en')
	if r == "break" :
		speak("bye")
	elif r == "hi" :
		speak("Hi, in tae Hwang")
		speak("say something")
		listen()
	else :
		speak(r)
		speak("say something")
		listen()

	return ""

speak("say something")
listen()