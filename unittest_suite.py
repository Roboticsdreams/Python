import unittest

from tests.leetcode.problems.test_program1 import TestTwoSum



def suite():
    suites = unittest.TestSuite()
    suites.addTest(unittest.TestLoader().loadTestsFromTestCase(TestTwoSum))
    return suites


if __name__ == '__main__':
    unittest.TextTestRunner(verbosity=2).run(suite())