import unittest
import sys
from io import StringIO
from hackerrank.introduction import division


class TestDivision(unittest.TestCase):
    def test_fun_division(self):
        output = StringIO()
        sys.stdout = output
        division.fun_division(4,3)
        sys.stdout = sys.__stdout__
        result = output.getvalue()
        self.assertEqual(result, "1\n1.3333333333333333\n")