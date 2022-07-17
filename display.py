from display_map import display_map
import time

TIME_A = 5
TIME_B = 15
TIME_C = 25

class display:
    
    _display = None
    _previous_t = None
    
    def __init__(self, display_handle):
        self._display = display_handle
        self._display.update_speed(2)
        
    def update(self, time_val=0):
        if self.is_display_update_needed(time_val):
            self._clear()
            self._legend()
            self._time(time_val)
            self._display.update()
    
    def is_display_update_needed(self, time_val):
        if self._previous_t == time_val:
            return False
        else:
            self._previous_t = time_val
            return True
        
    def _clear(self):
        self._display.pen(15)
        self._display.clear()
        self._display.pen(0)
        
    def _legend(self):
        self._display.thickness(1)
        
        items = [[display_map.POS_LEGEND_A_X, display_map.POS_LEGEND_A_Y, str(TIME_A)],
                [display_map.POS_LEGEND_B_X, display_map.POS_LEGEND_B_Y, str(TIME_B)],
                [display_map.POS_LEGEND_C_X, display_map.POS_LEGEND_C_Y, str(TIME_C)],
                [display_map.POS_LEGEND_UP_X, display_map.POS_LEGEND_UP_Y, "+1min"],
                [display_map.POS_LEGEND_DOWN_X, display_map.POS_LEGEND_DOWN_Y, "-1min"]]
       
        for x,y,txt in items: 
            self._display.text(txt, x, y, scale=0.6)
            
    def _time(self, val):
        self._display.thickness(6)
        self._display.text(str(val), 
                           display_map.POS_TIMER_X, 
                           display_map.POS_TIMER_Y,
                           scale=2.5)
        
