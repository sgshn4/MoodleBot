import structures
import time
from pynput import mouse
from pynput.keyboard import Key, Controller as keyboard

stageText = ["Click start Windows button.",
             "Type your browser name.",
             "Click on result of search.",
             "Open VSU site.",
             "Login.",
             "Open lecture to connect.",
             "Click \"Connect\" button.",
             "Click to turn on the sound button.",
             "Click menu button.",
             "Click \"Leave conference\" button.",
             "Click to URL bar.",
             "Saved. Now you can add subjects to connect."]
stage = 0
coordinates = []
xClick = 0
yClick = 0

#1 2 3 4 11
def nextStage():
    global stage
    global coordinates
    global xClick, yclick
    if (stage != 1 or stage != 2 or stage != 3 or stage != 4 or stage != 11):
        coordinates.append(structures.Point(xClick, yClick))
    stage = stage + 1


def on_click(x, y, button, pressed):
    global xClick
    global yClick
    print('{0} at {1}'.format(
        'Pressed' if pressed else 'Released',
        (x, y)))
    xClick = x
    yClick = y
    if not pressed:
        # Stop listener
        return False

def setClick():
    listener = mouse.Listener(on_click=on_click)
    listener.start()


