class PomodoroDraw():
      
    def __init__(self):
        self.full_cnt = 0
        self.empty_cnt = 0
        self.pom_flag = 0
        self.break_flag = 0

    def set_pomodoro_flag(self):
        self.pom_flag = 1
        self.break_flag = 0

    def set_break_flag(self):
        self.pom_flag = 0
        self.break_flag = 1

    def add_pom(self):
        if(self.pom_flag):
            self.empty_cnt += 1
        elif(self.break_flag):
            self.full_cnt += self.empty_cnt
            self.empty_cnt = 0
