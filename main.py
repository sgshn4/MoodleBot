import pyautogui
import time
import windows
import structures

from pynput.mouse import Button, Controller as mouse
from pynput.keyboard import Key, Controller as keyboard

p = structures.Point(100, 100)
print(p.getX(), p.getY())


mouse().position = (100, 100)
time.sleep(1)
mouse().position = (200, 200)