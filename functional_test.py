from timer import timer


def set_up_timer_and_countdown_5min():
    '''
    This functionality will be triggered after pressing a button
    '''
    t = timer()
    
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
    assert t.is_countdown_just_reached_zero() == True
    
    # After another one minute it is still zero
    t.tick()
    
    assert t.get_current_t() == 0
    
    # And buzzer is off
    assert t.is_countdown_just_reached_zero() == False
    

 
    
if __name__ == "__main__":
    print("Running functional tests")
    print(".",end='')
    set_up_timer_and_countdown_5min()
    
    print()