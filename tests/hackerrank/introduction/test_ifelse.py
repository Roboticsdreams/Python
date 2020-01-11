import unittest
import sys
from io import StringIO
from hackerrank.introduction import ifelse


class TestIfElse(unittest.TestCase):
    def test_if_else1(self):
        output = StringIO()
        sys.stdout = output
        ifelse.if_else(3)
        sys.stdout = sys.__stdout__
        result = output.getvalue()
        self.assertEqual(result, "Weird\n")

    def test_if_else2(self):
        output = StringIO()
        sys.stdout = output
        ifelse.if_else(8)
        sys.stdout = sys.__stdout__
        result = output.getvalue()
        self.assertEqual(result, "Weird\n")

    def test_if_else3(self):
        output = StringIO()
        sys.stdout = output
        ifelse.if_else(24)
        sys.stdout = sys.__stdout__
        result = output.getvalue()
        self.assertEqual(result, "Not Weird\n")