import speech_recognition

robot_ear = speech_recognition.Recognizer()
with speech_recognition.Microphone() as mic:
    print("Robot: I'm listening")
    audio = robot_ear.listen(mic, timeout=3, phrase_time_limit=3)

try:
    you = robot_ear.recognize_google(audio)
except:
    you= ""
print("You: "+ you)