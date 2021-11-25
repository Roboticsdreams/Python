import unittest

from tests.leetcode.problems.test_program1 import TestTwoSum
from tests.leetcode.problems.test_program2 import TestAddTwoNumbers
from tests.leetcode.problems.test_program3 import TestLongestSubstring
from tests.leetcode.problems.test_program4 import TestMedianSortedArrays
from tests.leetcode.problems.test_program5 import TestLongestPalindrome

def suite():
    suites = unittest.TestSuite()
    suites.addTest(unittest.TestLoader().loadTestsFromTestCase(TestTwoSum))
    suites.addTest(unittest.TestLoader().loadTestsFromTestCase(TestAddTwoNumbers))
    suites.addTest(unittest.TestLoader().loadTestsFromTestCase(TestLongestSubstring))
    suites.addTest(unittest.TestLoader().loadTestsFromTestCase(TestMedianSortedArrays))
    suites.addTest(unittest.TestLoader().loadTestsFromTestCase(TestLongestPalindrome))
    return suites


if __name__ == '__main__':
    unittest.TextTestRunner(verbosity=2).run(suite())