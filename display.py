from display_map import display_map

class display:
    
    _display = None
    
    def __init__(self, display_handle):
        self._display = display_handle
        
    def _clear(self):
        self._display.clear()
        
    def _legend(self):
        items = [[display_map.POS_LEGEND_A_X, display_map.POS_LEGEND_A_Y, "5"],
                [display_map.POS_LEGEND_B_X, display_map.POS_LEGEND_B_Y, "10"],
                [display_map.POS_LEGEND_C_X, display_map.POS_LEGEND_C_Y, "25"],
                [display_map.POS_LEGEND_UP_X, display_map.POS_LEGEND_UP_Y, "+1"],
                [display_map.POS_LEGEND_DOWN_X, display_map.POS_LEGEND_DOWN_Y, "-1"]]
       
        for x,y,txt in items: 
            self._display.text(txt, x, y)