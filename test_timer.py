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
        
        
if __name__ == "__main__":
    unittest.main()