from __future__ import print_function
import unittest
from sx.supply_chain_security import scs_case_1

class TestBugPartial(unittest.TestCase):
    def test_one_case(self):
        self.assertTrue(scs_case_1('x', True, 1, 3))
