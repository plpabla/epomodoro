import unittest
from timer import timer

class PomodoroDrawTest(unittest.TestCase):

    t = None
    
    def setUp(self) -> None:
        self.t = timer()
        self.t.set(0)
        return super().setUp()
        
    def tearDown(self) -> None:
        return super().tearDown()
    
    def test_start_with_zero_counters(self):
        self.assertEqual(self.t.pom.empty_cnt, 0)
        self.assertEqual(self.t.pom.full_cnt, 0)

    def test_start_with_no_flags_active(self):
        self.assertEqual(self.t.pom.break_flag, 0)
        self.assertEqual(self.t.pom.break_flag, 0)

    def test_set_pomodoro_flag_sets_and_clear_correct_flags(self):
        self.t.pom.set_pomodoro_flag()

        self.assertEqual(self.t.pom.break_flag, 0)
        self.assertEqual(self.t.pom.pom_flag, 1)

    def test_set_break_flag_sets_and_clear_correct_flags(self):
        self.t.pom.set_break_flag()

        self.assertEqual(self.t.pom.break_flag, 1)
        self.assertEqual(self.t.pom.pom_flag, 0)

    def test_countdown_with_pomodoro_flag_increases_empty_pomodoro_counter_from_0_to_1(self):
        self.t.pom.set_pomodoro_flag()
        self.t.set(1)
        self.t.tick()

        self.assertEqual(self.t.pom.empty_cnt, 1)
        self.assertEqual(self.t.pom.full_cnt, 0)

    def test_extra_ticks_doesnt_increase_pomodoros(self):
        self.t.pom.set_pomodoro_flag()
        self.t.set(1)
        self.t.tick()

        self.assertEqual(self.t.pom.empty_cnt, 1)
        self.assertEqual(self.t.pom.full_cnt, 0)

        self.t.tick()
        self.t.tick()

        self.assertEqual(self.t.pom.empty_cnt, 1)
        self.assertEqual(self.t.pom.full_cnt, 0)       

    def test_countdown_with_pomodoro_flag_increases_empty_pomodoro_counter_from_1_to_2(self):
        self.t.pom.empty_cnt = 1
        self.t.pom.set_pomodoro_flag()
        self.t.set(1)
        self.t.tick()

        self.assertEqual(self.t.pom.empty_cnt, 2)
        self.assertEqual(self.t.pom.full_cnt, 0)

    def test_countdown_with_break_flag_and_no_empty_pomodoros_does_nothing(self):
        self.t.pom.set_break_flag()
        self.t.set(1)
        self.t.tick()

        self.assertEqual(self.t.pom.empty_cnt, 0)
        self.assertEqual(self.t.pom.full_cnt, 0)

    def test_countdown_with_break_flag_fill_up_all_3_pomodoros(self):
        self.t.pom.empty_cnt = 3
        self.t.pom.set_break_flag()
        self.t.set(1)
        self.t.tick()

        self.assertEqual(self.t.pom.empty_cnt, 0)
        self.assertEqual(self.t.pom.full_cnt, 3)

    def test_countdown_with_pomodoro_adds_one_empty_to_already_full_pomodoros(self):
        self.t.pom.full_cnt = 3
        self.t.pom.set_pomodoro_flag()
        self.t.set(1)
        self.t.tick()

        self.assertEqual(self.t.pom.empty_cnt, 1)
        self.assertEqual(self.t.pom.full_cnt, 3)
        
if __name__ == "__main__":
    unittest.main()