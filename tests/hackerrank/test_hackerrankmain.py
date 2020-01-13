from unittest import mock
from hackerrank import hackerrankmain
import unittest


class TestHackerRankMain(unittest.TestCase):
    @mock.patch('hackerrank.introduction.intromain')
    def test_main(self, mock_intromain):
        result = hackerrankmain.hackerrankmain()
        expected = 1
        self.assertEqual(result, expected)