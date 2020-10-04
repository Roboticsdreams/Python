import unittest

from dailycodingproblem import dailycodingproblemmain


class TestDailyCodingProblemMain(unittest.TestCase):
    def test_main(self):
        result = dailycodingproblemmain.dailycodingproblemmain()
        expected = 1
        self.assertEqual(result, expected)
