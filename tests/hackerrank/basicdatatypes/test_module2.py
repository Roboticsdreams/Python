import unittest
import sys
from io import StringIO
from hackerrank.basicdatatypes import module2


class Test_Module2(unittest.TestCase):
    def test_method1(self):
        capturedOutput = StringIO()  # Create StringIO object
        sys.stdout = capturedOutput  #  and redirect stdout.
        module2.method1() # Call unchanged function.
        sys.stdout = sys.__stdout__   # Reset redirect.
        capturedout = capturedOutput.getvalue() # Now works as before.
        self.assertEqual(capturedout, "basicdatatypes module2 hello\n")

    def test_method2(self):
        capturedOutput = StringIO()  # Create StringIO object
        sys.stdout = capturedOutput  #  and redirect stdout.
        module2.method2() # Call unchanged function.
        sys.stdout = sys.__stdout__   # Reset redirect.
        capturedout = capturedOutput.getvalue() # Now works as before.
        self.assertEqual(capturedout, "basicdatatypes module2 world\n")