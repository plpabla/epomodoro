'''
Start countdown when button is pressed
Countdown and enable buzzer when reaching zero
'''

from display import display
from timer import timer
from machine import Timer
from machine import Pin
from buzzer import Buzzer
import badger2040

BUTTON_A = 12
BUTTON_B = 13
BUTTON_C = 14
BUTTON_UP = 15
BUTTON_DOWN = 11

badger = badger2040.Badger2040()
disp = display(badger)
buzzer = Buzzer()

def update_timer(tim):
    t.tick()
    disp.update(t.get_current_t())
    
    if(t.is_countdown_just_reached_zero()):
        buzzer.beep()
    

def btn_callback(pin):
    restart_counter_if_we_start(t.get_current_t())
    if pin==button_A:
        t.set(5)
    if pin==button_B:
        t.set(10)
    if pin==button_C:
        t.set(25)
    if pin==button_UP:
        t.set(t.get_current_t()+1)
    if pin==button_DOWN:
        t.tick()
    disp.update(t.get_current_t())


def restart_counter_if_we_start(t0):
    global tim
    if t0==0:
        tim.deinit()
        tim.init(period=60_000, mode=Timer.PERIODIC, callback=update_timer)


def setup(btn):
    button = Pin(btn, Pin.IN, Pin.PULL_DOWN)
    button.irq(trigger=Pin.IRQ_FALLING, handler=btn_callback)
    return button

button_A = setup(BUTTON_A)
button_B = setup(BUTTON_B)
button_C = setup(BUTTON_C)
button_UP = setup(BUTTON_UP)
button_DOWN = setup(BUTTON_DOWN)

t = timer()
t.set(0)
tim = Timer()

update_timer(None)
tim.init(period=60_000, mode=Timer.PERIODIC, callback=update_timer)