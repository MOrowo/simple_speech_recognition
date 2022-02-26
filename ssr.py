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
        color_list = ["test", "red", "green", "blue", "yellow", "exit"]
        if words in color_list:
            doColor(words)
        else:
            continue

    except sr.UnknownValueError:
        print("Sphinx could not understand audio")
    except sr.RequestError as e:
        print("Sphinx error; {0}".format(e))


def doColor(words):
    if words == "test":
        print("test has been executed")
        return True

    if words == "red":
        clear()
        set_all(255,0,0)
        show()
        return True

    if words == "green":
        clear()
        set_all(0,255,0)
        show()
        return True

    if words == "blue":
        clear()
        set_all(0,0,255)
        show()
        return True

    if words == "yellow":
        clear()
        set_all(115, 115, 0)
        show()
        return True

    if words == "exit":
        print("...")
        sleep(1)
        print("...")
        sleep(1)
        print("...")
        sleep(1)
        print("Goodbye")
        return False