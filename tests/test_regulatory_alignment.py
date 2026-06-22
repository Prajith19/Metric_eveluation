from __future__ import print_function
import unittest
from sx.regulatory_alignment import real_case_1

class TestBugPartial(unittest.TestCase):
    def test_one_case(self):
        self.assertTrue(real_case_1('x', True, 1, 3))
