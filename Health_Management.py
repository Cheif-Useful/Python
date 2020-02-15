# 2 Hour 
# 20 min water 
# 45 min Eyes
# 1hr body

import pyttsx3
import time

engine = pyttsx3.init('espeak')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[10].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def Pani():
    while True:
        print(time.asctime(time.localtime(time.time())))
        speak("Drink Water")
        water = input("Drink Water : ")
        water = water.lower()
        if water == "done":
            print("OK\n")
            speak("OK")
            break
        else:
            print("\nWrong Input\n")
            continue

def Aakhen():
    while True:
        print(time.asctime(time.localtime(time.time())))
        speak("Please Relax your Eyes")
        eyes = input("Please Relax your Eyes : ")
        eyes = eyes.lower()
        if eyes == "done":
            print("OK\n")
            speak("OK")
            break
        else:
            print("\nWrong Input\n")
            continue

def Body():
    while True:
        print(time.asctime(time.localtime(time.time())))
        speak("Do Some Physical Exercise")
        physical = input("Do Some Physical Exercise : ")
        physical = physical.lower()
        if physical == "done":
            print("OK\n")
            speak("OK")
            break
        else:
            print("\nWrong Input\n")
            continue

if __name__ == "__main__":
    speak("Hello Sir. I am Jarvis")
    Pani()
    time.sleep(20*60)
    Pani()
    time.sleep(20*60)
    Pani()
    time.sleep(5*60)
    Aakhen()
    time.sleep(15*60)
    Pani()
    Body()
    time.sleep(20*60)
    Pani()
    time.sleep(20*60)
    Pani()
    time.sleep(5*60)
    Aakhen()
    time.sleep(15*60)
    Pani()
    Body()
    speak("Two Hours Ended")
    print(time.asctime(time.localtime(time.time())))
    speak("Bye")