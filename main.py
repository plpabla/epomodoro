'''
Start countdown when button is pressed
Countdown and enable buzzer when reaching zero

TODO: Implement sleep/deepsleep to save the battery (https://github.com/ghubcoder/micropython-pico-deepsleep)
1. Sleep 60s between refresh
2. Sleep after reaching zero
Wakeup when button is pressed
'''

from display import display
from display_map import display_map
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
    disp.update(t.get_current_t(), t.pom.full_cnt, t.pom.empty_cnt)
    
    if(t.is_countdown_just_reached_zero()):
        buzzer.beep()
    

def btn_callback(pin):
    restart_counter_if_we_start(t.get_current_t())
    if pin==button_A:
        t.set(display_map.TIME_A)
        t.pom.set_break_flag()
    if pin==button_B:
        t.set(display_map.TIME_B)
        t.pom.set_break_flag()
    if pin==button_C:
        t.set(display_map.TIME_C)
        t.pom.set_pomodoro_flag()
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
