from unittest import mock
from hackerrank import hackerrankmain
import unittest


class TestHackerRankMain(unittest.TestCase):
    @mock.patch('hackerrank.introduction.introductionmain.main')
    def test_main(self, mock_main):
        result = hackerrankmain.main()
        expected = 1
        self.assertEqual(result, expected)