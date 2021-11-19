import unittest

from tests.leetcode.problems.test_program1 import TestTwoSum
from tests.leetcode.problems.test_program2 import TestAddTwoNumbers


def suite():
    suites = unittest.TestSuite()
    suites.addTest(unittest.TestLoader().loadTestsFromTestCase(TestTwoSum))
    suites.addTest(unittest.TestLoader().loadTestsFromTestCase(TestAddTwoNumbers))
    return suites


if __name__ == '__main__':
    unittest.TextTestRunner(verbosity=2).run(suite())