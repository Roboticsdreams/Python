import unittest
import sys
from io import StringIO
from hackerrank.introduction import module1


class Test_Module1(unittest.TestCase):
    def test_method1(self):
        capturedOutput = StringIO()  # Create StringIO object
        sys.stdout = capturedOutput  #  and redirect stdout.
        module1.method1() # Call unchanged function.
        sys.stdout = sys.__stdout__   # Reset redirect.
        capturedout = capturedOutput.getvalue() # Now works as before.
        self.assertEqual(capturedout, "introduction module1 hello\n")

    def test_method2(self):
        capturedOutput = StringIO()  # Create StringIO object
        sys.stdout = capturedOutput  #  and redirect stdout.
        module1.method2() # Call unchanged function.
        sys.stdout = sys.__stdout__   # Reset redirect.
        capturedout = capturedOutput.getvalue() # Now works as before.
        self.assertEqual(capturedout, "introduction module1 world\n")