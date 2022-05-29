import unittest
from unittest.mock import Mock
from display import display

class TimerTest(unittest.TestCase):
    
    display = None
    
    def setUp(self) -> None:
        self.display = display(MockDisplay())
        return super().setUp()
        
    def tearDown(self) -> None:
        return super().tearDown()
    
    def test_display_is_created(self):
        self.assertIsInstance(self.display._display, MockDisplay)
        
    def test_clear_function_calls_clear(self):
        self.display._clear()
        
        self.assertEqual(self.display._display.cnt_clear, 1)
        
    def test_legend_function_calls_text(self):
        self.display._legend()
        
        self.assertTrue(self.display._display.cnt_text > 0)
        
    
class MockDisplay():
    cnt_clear = 0
    cnt_text = 0
    
    def clear(self):
        self.cnt_clear += 1
    
    def text(self, message, x, y, scale=1.0, rotation=0.0):
        print(f"text in ({x},{y}): {message}")
        self.cnt_text += 1
    
    def glyph(self, char, x, y, scale=1.0, rotation=0.0):
        pass
    
    def measure_text(self, message, scale=1.0):
        pass
    
    def measure_glyph(self, char, scale=1.0):
        pass
    
    def font(self, font):
        pass
    