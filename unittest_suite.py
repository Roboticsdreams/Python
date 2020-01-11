import unittest

from tests.hackerrank.introduction.test_helloworld import TestHelloWorld
from tests.hackerrank.introduction.test_ifelse import TestIfElse
from tests.hackerrank.introduction.test_arithematicoperator import TestArithematicOperator
from tests.hackerrank.introduction.test_introductionmain import TestIntroductionMain
from tests.hackerrank.test_hackerrankmain import TestHackerRankMain


def suite():
    suites = unittest.TestSuite()
    suites.addTest(unittest.TestLoader().loadTestsFromTestCase(TestHelloWorld))
    suites.addTest(unittest.TestLoader().loadTestsFromTestCase(TestIfElse))
    suites.addTest(unittest.TestLoader().loadTestsFromTestCase(TestArithematicOperator))
    suites.addTest(unittest.TestLoader().loadTestsFromTestCase(TestIntroductionMain))
    suites.addTest(unittest.TestLoader().loadTestsFromTestCase(TestHackerRankMain))
    return suites


if __name__ == '__main__':
    unittest.TextTestRunner(verbosity=2).run(suite())