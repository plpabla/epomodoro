from machine import Pin
from machine import PWM
import time

class Buzzer():
    
    _pin = None
    
    def __init__(self):
        '''
        GPIO3 is used (INT label on the board)
        '''
        self._pin = PWM(Pin(3))
        self._pin.freq(2000)
        self._pin.duty_u16(0)
        
    def beep(self):
        PWM_000 = 0
        PWM_050 = 32768
        PWM_100 = 65535
        
        TIME_0S5 = 0.5
        TIME_1S = 1
        TIME_2S = 2
        
        seq = [[PWM_050, TIME_0S5],
               [PWM_000, TIME_1S],
               [PWM_050, TIME_1S],
               [PWM_000, TIME_1S],
               [PWM_050, TIME_1S]]
        
        for duty, time_s in seq:
            self._pin.duty_u16(duty)
            time.sleep(time_s)
        
        self._pin.duty_u16(PWM_000)