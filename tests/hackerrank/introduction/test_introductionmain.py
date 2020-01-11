import unittest
from hackerrank.introduction import introductionmain
from unittest import mock


class TestIntroductionMain(unittest.TestCase):
    @mock.patch('hackerrank.introduction.helloworld.fun_helloworld')
    @mock.patch('hackerrank.introduction.ifelse.fun_ifelse')
    @mock.patch('hackerrank.introduction.arithematicoperator.fun_arithematic')
    @mock.patch('hackerrank.introduction.division.fun_division')
    def test_introductionmain(self,mock_fun_helloworld,mock_fun_ifelse, mock_fun_arithematic,mock_fun_division):
        result = introductionmain.main()
        expected = 1
        self.assertEqual(result, expected)