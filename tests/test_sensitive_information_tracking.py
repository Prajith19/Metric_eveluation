from __future__ import print_function
import unittest
from sx.sensitive_information_tracking import sit_case_1

class TestBugPartial(unittest.TestCase):
    def test_one_case(self):
        self.assertTrue(sit_case_1('x', True, 1, 3))
