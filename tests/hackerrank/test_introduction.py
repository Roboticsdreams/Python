import unittest
import sys
from io import StringIO
from hackerrank import introduction
from unittest import mock

class TestIntroduction(unittest.TestCase):
    def setUp(self):
        self.intro = introduction.Introduction()

    def test_fun_helloworld(self):
        output = StringIO()
        sys.stdout = output
        self.intro.fun_helloworld()
        sys.stdout = sys.__stdout__
        result = output.getvalue()
        self.assertEqual(result, "Hello, World!\n")

    def test_fun_ifelse1(self):
        output = StringIO()
        sys.stdout = output
        self.intro.fun_ifelse(3)
        sys.stdout = sys.__stdout__
        result = output.getvalue()
        self.assertEqual(result, "Weird\n")

    def test_fun_ifelse2(self):
        output = StringIO()
        sys.stdout = output
        self.intro.fun_ifelse(8)
        sys.stdout = sys.__stdout__
        result = output.getvalue()
        self.assertEqual(result, "Weird\n")

    def test_fun_ifelse3(self):
        output = StringIO()
        sys.stdout = output
        self.intro.fun_ifelse(24)
        sys.stdout = sys.__stdout__
        result = output.getvalue()
        self.assertEqual(result, "Not Weird\n")

    def test_arithematicoperatpr(self):
        output = StringIO()
        sys.stdout = output
        self.intro.fun_arithematicoperators(3,2)
        sys.stdout = sys.__stdout__
        result = output.getvalue()
        self.assertEqual(result, "5\n1\n6\n")

    def test_fun_division(self):
        output = StringIO()
        sys.stdout = output
        self.intro.fun_division(4,3)
        sys.stdout = sys.__stdout__
        result = output.getvalue()
        self.assertEqual(result, "1\n1.3333333333333333\n")

    @mock.patch('hackerrank.introduction.Introduction')
    def test_intromain(self, mock_Introduction):
        result = introduction.intromain()
        expected = 1
        self.assertEqual(result, expected)