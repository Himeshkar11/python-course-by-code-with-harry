from gtts import gTTS

text = "こんばんわ"

tts = gTTS(text=text, lang="ja")
tts.save("hello.mp3")