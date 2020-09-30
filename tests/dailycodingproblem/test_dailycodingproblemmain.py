from unittest import mock
from dailycodingproblem import dailycodingproblemmain
import unittest


class TestDailyCodingProblemMain(unittest.TestCase):
    @mock.patch('dailycodingproblem.google.googlemain')
    def test_main(self, mock_GoogleMain):
        result = dailycodingproblemmain.dailycodingproblemmain()
        expected = 1
        self.assertEqual(result, expected)