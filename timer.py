class timer():
    
    current_timer_vale = 0
    just_reached_zero_flag = False
    
    def __init__(self):
        pass
    
    def get_current_t(self):
        return self.current_timer_vale
    
    def set(self, new_time_s):
        self.current_timer_vale = new_time_s
        self.just_reached_zero_flag = False
        
    def tick(self):
        if(self.current_timer_vale>0):
            self.current_timer_vale -= 1
            if(self.current_timer_vale==0):
                self.just_reached_zero_flag = True
    
    def is_countdown_just_reached_zero(self):
        '''
        Returns True if timer reached zero and this function wasn't called since that event
        '''
        result = self.just_reached_zero_flag
        self.just_reached_zero_flag = False
        return result