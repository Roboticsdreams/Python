import unittest
from hackerrank.introduction import introductionmain
from unittest import mock


class TestIntroductionMain(unittest.TestCase):
    @mock.patch('hackerrank.introduction.helloworld.sayhelloworld')
    @mock.patch('hackerrank.introduction.ifelse.if_else')
    @mock.patch('hackerrank.introduction.arithematicoperator.arithop')
    def test_introductionmain(self,mock_sayhelloworld,mock_if_else, mock_arithop):
        result = introductionmain.main()
        expected = 1
        self.assertEqual(result, expected)