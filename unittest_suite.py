import unittest

from tests.dailycodingproblem.test_dailycodingproblemmain import TestDailyCodingProblemMain
from tests.dailycodingproblem.test_google import TestGoogle
from tests.dailycodingproblem.test_uber import TestUber


def suite():
    suites = unittest.TestSuite()
    suites.addTest(unittest.TestLoader().loadTestsFromTestCase(TestGoogle))
    suites.addTest(unittest.TestLoader().loadTestsFromTestCase(TestUber))
    suites.addTest(unittest.TestLoader().loadTestsFromTestCase(TestDailyCodingProblemMain))
    return suites


if __name__ == '__main__':
    unittest.TextTestRunner(verbosity=2).run(suite())