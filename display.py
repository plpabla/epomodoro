from display_map import display_map
import time

class display:
    
    _display = None
    _previous_t = None
    
    def __init__(self, display_handle):
        self._display = display_handle
        self._display.update_speed(2)
        
    def update(self, time_val=0, full=0, empty=0, force=False):
        if self.is_display_update_needed(time_val) or force:
            self._clear()
            self._legend()
            self._time(time_val)
            self._pomodoros(full, empty)
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
        
        items = [[display_map.POS_LEGEND_A_X, display_map.POS_LEGEND_A_Y, str(display_map.TIME_A)],
                [display_map.POS_LEGEND_B_X, display_map.POS_LEGEND_B_Y, str(display_map.TIME_B)],
                [display_map.POS_LEGEND_C_X, display_map.POS_LEGEND_C_Y, str(display_map.TIME_C)],
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
        
    def _pomodoros(self, full, empty):
        pos_x = display_map.POS_POM_X

        self._display.thickness(10)
        for _ in range(full):        
            self._display.text("O", pos_x, display_map.POS_POM_Y)
            pos_x += display_map.POS_POM_DELTA_X

        self._display.thickness(2)
        for _ in range(empty):
            self._display.text("O", pos_x, display_map.POS_POM_Y)
            pos_x += display_map.POS_POM_DELTA_X
