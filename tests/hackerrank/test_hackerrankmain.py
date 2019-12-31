import unittest
import sys
from io import StringIO
from hackerrank import hackerrankmain


class Test_HackerRankMain(unittest.TestCase):
    def test_main(self):
        capturedOutput = StringIO()  # Create StringIO object
        sys.stdout = capturedOutput  #  and redirect stdout.
        hackerrankmain.main() # Call unchanged function.
        sys.stdout = sys.__stdout__   # Reset redirect.
        capturedout = capturedOutput.getvalue() # Now works as before.
        expected = ("basicdatatypes module1 hello\n"
                     "basicdatatypes module1 world\n"
                     "basicdatatypes module2 hello\n"
                     "basicdatatypes module2 world\n"
                     "introduction module1 hello\n"
                     "introduction module1 world\n"
                     "introduction module2 hello\n"
                     "introduction module2 world\n")
        self.assertEqual(capturedout, expected);