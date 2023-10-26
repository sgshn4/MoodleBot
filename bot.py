from pynput.mouse import Button, Controller as mouse
from pynput.keyboard import Key, Controller as keyboard
import time

def run(lectures, coordinates, browserName):
    mouse.position = (coordinates[0].x, coordinates[0].y)
    mouse.click(Button.left, 1)
    mouse.position = (coordinates[1].x, coordinates[1].y)
    mouse.click(Button.left, 1)
    keyboard.type(browserName)
    mouse.position = (coordinates[2].x, coordinates[3].y)
    mouse.click(Button.left, 1)
    for i in range(len(lectures)):
        mouse.position = (coordinates[11].x, coordinates[11].y)
        mouse.click(Button.left, 1)
        keyboard.type(lectures[i])
        keyboard.press("Enter")