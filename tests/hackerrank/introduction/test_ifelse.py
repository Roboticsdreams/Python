import unittest
import sys
from io import StringIO
from hackerrank.introduction import ifelse


class TestIfElse(unittest.TestCase):
    def test_fun_ifelse1(self):
        output = StringIO()
        sys.stdout = output
        ifelse.fun_ifelse(3)
        sys.stdout = sys.__stdout__
        result = output.getvalue()
        self.assertEqual(result, "Weird\n")

    def test_fun_ifelse2(self):
        output = StringIO()
        sys.stdout = output
        ifelse.fun_ifelse(8)
        sys.stdout = sys.__stdout__
        result = output.getvalue()
        self.assertEqual(result, "Weird\n")

    def test_fun_ifelse3(self):
        output = StringIO()
        sys.stdout = output
        ifelse.fun_ifelse(24)
        sys.stdout = sys.__stdout__
        result = output.getvalue()
        self.assertEqual(result, "Not Weird\n")