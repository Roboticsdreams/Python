import unittest
import sys
from io import StringIO
from hackerrank.introduction import helloworld


class TestHelloWorld(unittest.TestCase):
    def test_sayhelloworld(self):
        output = StringIO()  # Create StringIO object
        sys.stdout = output  #  and redirect stdout.
        helloworld.sayhelloworld() # Call unchanged function.
        sys.stdout = sys.__stdout__   # Reset redirect.
        result = output.getvalue() # Now works as before.
        self.assertEqual(result, "Hello, World!\n")