class timer():
    
    current_timer_vale = 0
    
    def get_current_t(self):
        return self.current_timer_vale
    
    def set(self, new_time_s):
        self.current_timer_vale = new_time_s