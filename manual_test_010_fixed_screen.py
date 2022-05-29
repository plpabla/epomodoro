'''
This test will display main screen with constant value

'''

from display import display
import badger2040

badger = badger2040.Badger2040()
disp = display(badger)

disp.update(10)
