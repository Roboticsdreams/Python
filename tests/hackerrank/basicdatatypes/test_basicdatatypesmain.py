import unittest
import sys
from io import StringIO
from hackerrank.basicdatatypes import basicdatatypesmain


class Test_BasicDataTypeMain(unittest.TestCase):
    def test_main(self):
        capturedOutput = StringIO()  # Create StringIO object
        sys.stdout = capturedOutput  #  and redirect stdout.
        basicdatatypesmain.main() # Call unchanged function.
        sys.stdout = sys.__stdout__   # Reset redirect.
        capturedout = capturedOutput.getvalue() # Now works as before.
        expected = ("basicdatatypes module1 hello\n"
                    "basicdatatypes module1 world\n"
                    "basicdatatypes module2 hello\n"
                    "basicdatatypes module2 world\n")
        self.assertEqual(capturedout, expected);