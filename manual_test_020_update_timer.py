'''
This test will display main and starts counting down (not in real time only faster)

Note: after reaching zero it should stay at that value
'''

from display import display
from timer import timer
from machine import Timer
import badger2040

badger = badger2040.Badger2040()
disp = display(badger)

def update_timer(tim):
    disp.update(t.get_current_t())
    t.tick()


t = timer()
t.set(5)
tim = Timer()

tim.init(period=10_000, mode=Timer.PERIODIC, callback=update_timer)


