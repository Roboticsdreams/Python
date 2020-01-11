import unittest
import sys
from io import StringIO
from hackerrank.introduction import arithematicoperator


class TestArithematicOperator(unittest.TestCase):
    def test_arithop(self):
        output = StringIO()
        sys.stdout = output
        arithematicoperator.fun_arithematic(3,2)
        sys.stdout = sys.__stdout__
        result = output.getvalue()
        self.assertEqual(result, "5\n1\n6\n")