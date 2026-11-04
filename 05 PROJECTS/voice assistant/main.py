from gtts import gTTS

text = "sai erripooka"

tts = gTTS(text=text, lang="en")
tts.save("hello.mp3")