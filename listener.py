import keyboard
import time
import os
def delay():
    os.startfile("lock.pyw")
while True:
    if keyboard.is_pressed('Windows')and keyboard.is_pressed('`'):
        delay()
        time.sleep(5)
