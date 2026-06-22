from __future__ import print_function
import unittest
from sx.best_practice_compliance import bpc_case_1

class TestBugPartial(unittest.TestCase):
    def test_one_case(self):
        self.assertTrue(bpc_case_1('x', True, 1, 3))
