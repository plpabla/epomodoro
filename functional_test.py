from timer import timer


def SetUpTimerAndCountDown5minCalledAfterPressingButtonA():
    t = timer()
    # I press "A" 
    # TODO: add this test case
    
    # Timer is set up to 5
    t.set(5)
    
    # I see "5" on a display
    assert t.get_current_t() == 5
    
    # I wait 1 minute
    t.tick()
    
    # I see "4" on a display
    assert t.get_current_t() == 4
    
    # I wait another 4 minutes
    for i in range(4):
        t.tick()
    
    # I see "0" on a display
    assert t.get_current_t() == 0
    
    # I hear buzzer
    # TODO: check if it was trigerred
    
    # After another one minute it is still zero
    t.tick()
    
    assert t.get_current_t() == 0
    
    
if __name__ == "__main__":
    SetUpTimerAndCountDown5minCalledAfterPressingButtonA()