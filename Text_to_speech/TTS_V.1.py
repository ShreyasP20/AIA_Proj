import pyttsx3

engine = pyttsx3.init()

rate = engine.getProperty('rate')
engine.setProperty('rate', rate - 50)  

volume = engine.getProperty('volume')
engine.setProperty('volume', 0.9)  


engine.setProperty('pitch', 0.8) 

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

engine.say("Hello, how are you today?")
engine.say("My current speaking rate is " + str(rate))
engine.runAndWait()
engine.stop()
isl="Going to sleep"

engine.save_to_file(f"Translation for:{isl}", "audio.mp3")
engine.runAndWait()
