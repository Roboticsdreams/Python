import io
import sys
import unittest

from dailycodingproblem import apple
from unittest import mock

class TestApple(unittest.TestCase):
    def setUp(self):
        self.appleobj = apple.Apple()

    def test_scheduler_Test01(self):
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        self.appleobj.scheduler(self.appleobj.hello_world, 1)
        result = capturedOutput.getvalue()
        expected = "Hello World\n"
        self.assertEqual(result, expected)

    @mock.patch('dailycodingproblem.apple.Apple')
    def test_applemain(self, mock_Apple):
        result = apple.applemain()
        expected = 1
        self.assertEqual(result, expected)
