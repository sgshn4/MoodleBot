import pyautogui
import time
import homeScreen

from pynput.mouse import Button, Controller as mouse
from pynput.keyboard import Key, Controller as keyboard

homeScreen.show()

mouse().position = (100, 100)
time.sleep(1)
mouse().position = (200, 200)