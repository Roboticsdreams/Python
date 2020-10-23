import unittest
from unittest import mock

from dailycodingproblem import google
from dailycodingproblem.commonutils import Node


class TestGoogle(unittest.TestCase):
    def setUp(self):
        self.googleobj = google.Google()

    def test_containspairwithsum_Test01(self):
        arr = [10, 15, 3, 7]
        total = 17
        result = self.googleobj.containspairwithsum(arr, total)
        expected = True
        self.assertEqual(result, expected)

    def test_containspairwithsum_Test02(self):
        arr = [10, 15, 3, 7]
        total = 11
        result = self.googleobj.containspairwithsum(arr, total)
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

    def test_nonrepeatingelement_Test01(self):
        list = [6, 1, 3, 3, 3, 6, 6]
        result = self.googleobj.nonrepeatingelement(list)
        expected = 1
        self.assertEqual(result, expected)

    @mock.patch('dailycodingproblem.google.Google')
    def test_googlemain(self, mock_Google):
        result = google.googlemain()
        expected = 1
        self.assertEqual(result, expected)
