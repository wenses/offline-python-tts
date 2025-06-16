import pyttsx3 as tts

word=input("What to say: ")
#word='blabla'
speak=tts.init()
speak.say(word)
speak.runAndWait()

print(dir(speak))