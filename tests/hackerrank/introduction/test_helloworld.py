import unittest
import sys
from io import StringIO
from hackerrank.introduction import helloworld


class TestHelloWorld(unittest.TestCase):
    def test_fun_helloworld(self):
        output = StringIO()
        sys.stdout = output
        helloworld.fun_helloworld()
        sys.stdout = sys.__stdout__
        result = output.getvalue()
        self.assertEqual(result, "Hello, World!\n")