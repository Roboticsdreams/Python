import unittest
from unittest import mock

from dailycodingproblem import janestreet

class TestJaneStreet(unittest.TestCase):
    def setUp(self):
        self.jsobj = janestreet.JaneStreet()

    def test_carCons(self):
        result = self.jsobj.car(self.jsobj.cons(3, 4))
        expected = 3
        self.assertEqual(result, expected)

    def test_cdrCons(self):
        result = self.jsobj.cdr(self.jsobj.cons(3, 4))
        expected = 4
        self.assertEqual(result, expected)

    @mock.patch('dailycodingproblem.janestreet.JaneStreet')
    def test_janestreetmain(self, mock_JaneStreet):
        result = janestreet.janestreetmain()
        expected = 1
        self.assertEqual(result, expected)
