import speech_recognition
import pyttsx3

robot_ear = speech_recognition.Recognizer()
with speech_recognition.Microphone() as mic:
    print("Robot: I'm listening")
    audio = robot_ear.listen(mic, timeout=3, phrase_time_limit=3)

try:
    you = robot_ear.recognize_google(audio)
except:
    you= ""
print("You: "+ you)

if you == "":
    robot_brain = "I can't hear you, try agian"
elif you == "hello":
    robot_brain= "hello Binhtt"
elif you == "who am I":
    robot_brain= "Binh handsome"
elif you == "Lock screen":
    robot_brain= "Okay!"
elif you == "open Spotify":
    robot_brain= "Okay!"
else:
     robot_brain ="I'm fine thank you and you"
print(robot_brain)


robot_mounth = pyttsx3.init()
robot_mounth.say(robot_brain)
robot_mounth.runAndWait()