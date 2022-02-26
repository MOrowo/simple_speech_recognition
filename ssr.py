import speech_recognition as sr
from datetime import date
from time import sleep
from blinkt import set_pixel, set_brightness, show, clear, set_all

r = sr.Recognizer()
mic = sr.Microphone()

print("hello")

while True:
    try:
        with mic as source:
            audio = r.listen(source)
        words = r.recognize_sphinx(audio)
        print(words)

        if words == "test":
            print("test has been executed")

        if words == "red":
            clear()
            set_all(255,0,0)
            show()

        if words == "green":
            clear()
            set_all(0,255,0)
            show()

        if words == "blue":
            clear()
            set_all(0,0,255)
            show()

        if words == "yellow":
            clear()
            set_all(115, 115, 0)
            show()

        if words == "exit":
            print("...")
            sleep(1)
            print("...")
            sleep(1)
            print("...")
            sleep(1)
            print("Goodbye")
            break
        
    except sr.UnknownValueError:
        print("Sphinx could not understand audio")
    except sr.RequestError as e:
        print("Sphinx error; {0}".format(e))