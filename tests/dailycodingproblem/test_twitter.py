import unittest
from unittest import mock

from dailycodingproblem import twitter


class TestTwitter(unittest.TestCase):
    def setUp(self):
        self.twitterobj = twitter.Twitter()

    def test_autocomplete_Test01(self):
        str = "de"
        orglist = ['dog', 'deer', 'deal']
        result = self.twitterobj.autocomplete(str, orglist)
        expected = ['deer', 'deal']
        self.assertEqual(result, expected)

    def test_autocomplete_Test02(self):
        str = "og"
        orglist = ['dog', 'deer', 'deal']
        result = self.twitterobj.autocomplete(str, orglist)
        expected = 0
        self.assertEqual(result, expected)

    def test_autocomplete_Test03(self):
        str = "dog"
        orglist = ['dog', 'deer', 'deal']
        result = self.twitterobj.autocomplete(str, orglist)
        expected = -1
        self.assertEqual(result, expected)

    @mock.patch('dailycodingproblem.twitter.Twitter')
    def test_twittermain(self, mock_Twitter):
        result = twitter.twittermain()
        expected = 1
        self.assertEqual(result, expected)