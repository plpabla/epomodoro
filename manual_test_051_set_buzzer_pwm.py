from machine import Pin
from machine import PWM
import time
import badger2040

badger = badger2040.Badger2040()

badger.pen(0)
badger.text("Buzzer test",20,20)
badger.update()

buzzer = PWM(Pin(3))
buzzer.freq(4000)

while True:
    buzzer.duty_u16(32000)
    time.sleep(1)
    buzzer.duty_u16(0)
    time.sleep(5)
    