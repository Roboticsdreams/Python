import unittest
from unittest import mock

from dailycodingproblem import google
from dailycodingproblem.commonutils import Node


class TestGoogle(unittest.TestCase):
    def setUp(self):
        self.googleobj = google.Google()

    def test_containsPairWithSum_Test01(self):
        listinput = [10, 15, 3, 7]
        total = 17
        result = self.googleobj.containsPairWithSum(listinput, total)
        expected = True
        self.assertEqual(result, expected)

    def test_containsPairWithSum_Test02(self):
        listinput = [10, 15, 3, 7]
        total = 11
        result = self.googleobj.containsPairWithSum(listinput, total)
        expected = False
        self.assertEqual(result, expected)

    def test_seralizeDeseralize_Test01(self):
        node = Node('root', Node('left', Node('left.left')), Node('right'))
        result = self.googleobj.serialize(node)
        result1 = self.googleobj.deserialize(result).left.left.val
        expected = "left.left"
        self.assertEqual(result1, expected)

    def test_seralizeDeseralize_Test02(self):
        node = None
        result = self.googleobj.serialize(node)
        result1 = self.googleobj.deserialize(result)
        expected = None
        self.assertEqual(result1, expected)

    @mock.patch('dailycodingproblem.google.Google')
    def test_googlemain(self, mock_Google):
        result = google.googlemain()
        expected = 1
        self.assertEqual(result, expected)
