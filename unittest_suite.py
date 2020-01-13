import unittest

from tests.hackerrank.test_introduction import TestIntroduction
from tests.hackerrank.test_hackerrankmain import TestHackerRankMain


def suite():
    suites = unittest.TestSuite()
    suites.addTest(unittest.TestLoader().loadTestsFromTestCase(TestIntroduction))
    suites.addTest(unittest.TestLoader().loadTestsFromTestCase(TestHackerRankMain))
    return suites


if __name__ == '__main__':
    unittest.TextTestRunner(verbosity=2).run(suite())