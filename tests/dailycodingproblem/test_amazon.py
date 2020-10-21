import unittest
from unittest import mock

from dailycodingproblem import amazon


class TestAmazon(unittest.TestCase):
    def setUp(self):
        self.amazonobj = amazon.Amazon()

    def test_staircase_Test01(self):
        result = self.amazonobj.staircase(5, [1,3,5])
        expected = 5
        self.assertEqual(result, expected)

    @mock.patch('dailycodingproblem.amazon.Amazon')
    def test_amazonmain(self, mock_Amazon):
        result = amazon.amazonmain()
        expected = 1
        self.assertEqual(result, expected)
