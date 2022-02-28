### Simple voice recognition with Raspberry Pi
---

## Equipments
1. Raspberry pi with 40 pins header
2. USB microphone
3. SD card
4. [Blinkt!](https://shop.pimoroni.com/products/blinkt?variant=22408658695)

## How to do
1. Make sure you have a Raspberry Pi with an installed OS.
2. Make sure you have Python 3 installed on the Pi.<br>
`python --version`
3. Clone this git repository.<br>
`git clone https://github.com/MOrowo/simple_speech_recognition.git`
4. Install [SpeechRecognition](https://pypi.org/project/SpeechRecognition/) using pip.<br>
`pip install speechrecognition`
5. Change directory to the directory where this clone is located.<br>
`cd simple_speech_recognition`
6. Run the script.<br>
`python ssr.py`
