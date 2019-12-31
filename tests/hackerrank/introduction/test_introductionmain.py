import unittest
import sys
from io import StringIO
from hackerrank.introduction import introductionmain


class Test_IntroductionMain(unittest.TestCase):
    def test_main(self):
        capturedOutput = StringIO()  # Create StringIO object
        sys.stdout = capturedOutput  #  and redirect stdout.
        introductionmain.main() # Call unchanged function.
        sys.stdout = sys.__stdout__   # Reset redirect.
        capturedout = capturedOutput.getvalue() # Now works as before.
        expected = ("introduction module1 hello\n"
                    "introduction module1 world\n"
                    "introduction module2 hello\n"
                    "introduction module2 world\n")
        self.assertEqual(capturedout, expected);