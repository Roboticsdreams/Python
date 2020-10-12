import unittest
from unittest import mock

from dailycodingproblem import facebook

class TestFacebook(unittest.TestCase):
    def setUp(self):
        self.fbobj = facebook.Facebook()

    def test_numDecodings_Test01(self):
        result = self.fbobj.numDecodings("111")
        expected = 3
        self.assertEqual(result, expected)

    def test_numDecodings_Test02(self):
        result = self.fbobj.numDecodings("1")
        expected = 1
        self.assertEqual(result, expected)

    def test_numDecodings_Test03(self):
        result = self.fbobj.numDecodings("0")
        expected = 0
        self.assertEqual(result, expected)

    @mock.patch('dailycodingproblem.facebook.Facebook')
    def test_facebookmain(self, mock_Facebook):
        result = facebook.facebookmain()
        expected = 1
        self.assertEqual(result, expected)
