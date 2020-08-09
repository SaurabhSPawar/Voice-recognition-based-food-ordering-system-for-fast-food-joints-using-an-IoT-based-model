import speech_recognition as spr
import pyttsx3
from playsound import playsound
import time
def  recorddata():
    print(" listening ....")
    with spr.Microphone() as source:
            r.adjust_for_ambient_noise(source)
            sound = r.listen(source, timeout=1,phrase_time_limit=9)
            print("Time Over")
            playsound('bell.mp3')
            time.sleep(1)
            print("Text:"+r.recognize_google(sound))
    mode_choice = r.recognize_google(sound)
    return mode_choice
engine = pyttsx3.init()
engine.setProperty('rate', 170)    # Speed percent (can go over 100)
engine.setProperty('volume', 0.9)
r = spr.Recognizer()
r.pause_threshold = 0.6
microphone = spr.Microphone()
engine.say("Welcome  ")
engine.runAndWait()
time.sleep(2)
engine.say("Do you want to continue ?")
engine.runAndWait()
usr_choice = 1
flag=1
with spr.Microphone() as source:
    print("Do you want to continue ?")
    print("listening.... ")
    r.adjust_for_ambient_noise(source)
    sound = r.listen(source, timeout=18,phrase_time_limit=10)
    playsound('bell.mp3')
    time.sleep(1)
try:
    print("Text"+r.recognize_google(sound));
    user_sound = r.recognize_google(sound)
    if(user_sound == "yes" or user_sound ==   "ya" or user_sound == "yes yes"):
        print("todays offers are")
        
    elif(user_sound == "No"):
        print("todays offers are:")
       
    else:
        print("sorry,I am not understand")  
except:
    print("error")
    engine.say("Sorry ,Something Went wrong")
    engine.runAndWait()
