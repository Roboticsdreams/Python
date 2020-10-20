import unittest
from unittest import mock

from dailycodingproblem import uber


class TestUber(unittest.TestCase):
    def setUp(self):
        self.uberobj = uber.Uber()

    def test_productArray_Test01(self):
        listinput = [1, 2, 3, 4, 5]
        result = self.uberobj.productArray(listinput)
        expected = [120, 60, 40, 30, 24]
        self.assertEqual(result, expected)

    @mock.patch('dailycodingproblem.uber.Uber')
    def test_ubermain(self, mock_Uber):
        result = uber.ubermain()
        expected = 1
        self.assertEqual(result, expected)