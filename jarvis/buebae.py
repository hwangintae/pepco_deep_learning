from gtts import gTTS
import os
tts = gTTS('안녕하세요 브베 형님 저는 결혼정보회사에서 만난 베트남 처녀에요', lang = 'ko')
tts.save("buebae.mp3")
os.system("buebae.mp3")