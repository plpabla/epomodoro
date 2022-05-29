from machine import Pin
import time
import badger2040

badger = badger2040.Badger2040()

badger.pen(0)
badger.text("Buzzer test",20,20)
badger.update()

buzzer = Pin(3, Pin.OUT, None)

while True:
    buzzer.value(1)
    time.sleep(1)
    buzzer.value(0)
    time.sleep(5)
    