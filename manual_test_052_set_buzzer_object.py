import time
import badger2040
from buzzer import Buzzer

badger = badger2040.Badger2040()

badger.pen(0)
badger.text("Hello",20,20)
badger.update()

buzzer = Buzzer()

while True:
    buzzer.beep()
    time.sleep(10)