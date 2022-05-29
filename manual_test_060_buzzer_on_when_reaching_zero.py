'''
Countdown and enable buzzer when reaching zero
'''

from display import display
from timer import timer
from machine import Timer
from buzzer import Buzzer
import badger2040

badger = badger2040.Badger2040()
disp = display(badger)
buzzer = Buzzer()

def update_timer(tim):
    disp.update(t.get_current_t())
    if(t.is_countdown_just_reached_zero()):
        buzzer.beep()
    # FIXME: tick sets the flag which is being checked, so now order is first to check flag, then call tick. It should be other way around as right now alarm is beeping at t=1 not t=0    
    t.tick()


t = timer()
t.set(5)
tim = Timer()

update_timer(None)
tim.init(period=2_000, mode=Timer.PERIODIC, callback=update_timer)


