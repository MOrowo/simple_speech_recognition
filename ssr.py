import speech_recognition as sr
from time import sleep
from blinkt import set_pixel, set_brightness, show, clear, set_all

r = sr.Recognizer()
mic = sr.Microphone()

# Display color on the blinkt
# @param words - string
def display_color(words):
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

while True:

    try:
        # Use microphone
        with mic as source:
            audio = r.listen(source)
        words = r.recognize_google(audio)

        # Validation the voice command
        color_list = ["test", "red", "green", "blue", "yellow", "exit"]
        if words in color_list:
            display_color(words)
        else:
            continue

    except sr.UnknownValueError:
        print("Could not understand audio")
    except sr.RequestError as e:
        print("Google error; {0}".format(e))