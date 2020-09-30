import unittest
import sys
from io import StringIO
from dailycodingproblem import google
from unittest import mock


class TestGoogle(unittest.TestCase):
    def setUp(self):
        self.googleobj = google.Google()

    def test_containsPairWithSum_Test01(self):
        listinput = [10, 15, 3, 7]
        total = 17
        result = self.googleobj.containsPairWithSum(listinput,total)
        expected = True
        self.assertEqual(result, expected)

    def test_containsPairWithSum_Test02(self):
        listinput = [10, 15, 3, 7]
        total = 11
        result = self.googleobj.containsPairWithSum(listinput,total)
        expected = False
        self.assertEqual(result, expected)

    @mock.patch('dailycodingproblem.google.Google')
    def test_intromain(self, mock_Google):
        result = google.googlemain()
        expected = 1
        self.assertEqual(result, expected)
