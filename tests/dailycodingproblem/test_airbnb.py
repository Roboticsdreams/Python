import unittest
from unittest import mock

from dailycodingproblem import airbnb


class TestAirbnb(unittest.TestCase):
    def setUp(self):
        self.airbnbobj = airbnb.Airbnb()

    def test_maxSum_Test01(self):
        result = self.airbnbobj.maxSum([2, 4, 6, 2, 5])
        expected = 13
        self.assertEqual(result, expected)

    def test_maxSum_Test02(self):
        result = self.airbnbobj.maxSum([5, 1, 1, 5])
        expected = 11
        self.assertEqual(result, expected)

    def test_maxSum_Test03(self):
        result = self.airbnbobj.maxSum([5, 125, 1, 3, 1])
        expected = 133
        self.assertEqual(result, expected)

    @mock.patch('dailycodingproblem.airbnb.Airbnb')
    def test_airbnbmain(self, mock_Airbnb):
        result = airbnb.airbnbmain()
        expected = 1
        self.assertEqual(result, expected)
