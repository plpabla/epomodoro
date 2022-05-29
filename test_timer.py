import unittest
from timer import timer

class TimerTest(unittest.TestCase):

    t = None
    
    def setUp(self) -> None:
        self.t = timer()
        return super().setUp()
        
    def tearDown(self) -> None:
        return super().tearDown()
    
    def test_timer_initialized_with_zero(self):
        self.assertEqual(self.t.get_current_t(), 0)
        
    def test_set_timer_for_1(self):
        self.t.set(1)
        
        self.assertEqual(self.t.get_current_t(), 1)
    
    def _set_and_tick(self, val):
        self.t.set(val)
        self.t.tick()
        
    def test_tick_decrease_5_to_4(self):
        self._set_and_tick(5)
        
        self.assertEqual(self.t.get_current_t(), 4)
        
    def test_tick_decrease_1_to_0(self):
        self._set_and_tick(1)
        
        self.assertEqual(self.t.get_current_t(), 0)
        
    def test_tick_keeps_zero(self):
        self._set_and_tick(0)
        
        self.assertEqual(self.t.get_current_t(), 0)
        
    def test_after_set_flag_reached_zero_is_off(self):
        self.t.set(1)
        
        self.assertFalse(self.t.is_countdown_just_reached_zero())
        
    def test_after_tick_zero_reached_flag_is_on_then_off(self):
        self._set_and_tick(1)
        
        self.assertTrue(self.t.is_countdown_just_reached_zero())
        
        self.t.tick()
        
        self.assertFalse(self.t.is_countdown_just_reached_zero())
        
    def test_reached_zero_not_called_check_set_timer_and_just_reached_zero_flag_is_off(self):
        self._set_and_tick(1)
        self._set_and_tick(5)
        
        self.assertFalse(self.t.is_countdown_just_reached_zero())
        
if __name__ == "__main__":
    unittest.main()