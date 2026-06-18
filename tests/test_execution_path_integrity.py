from __future__ import print_function
import unittest
from sa.execution_path_integrity import epi_case_1

class TestBugPartial(unittest.TestCase):
    def test_one_case(self):
        self.assertTrue(epi_case_1('x', True, 1, 3))
