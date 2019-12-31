import unittest

from tests.hackerrank.basicdatatypes.test_module1 import Test_Module1 as basicdatatypes_test_module1
from tests.hackerrank.basicdatatypes.test_module2 import Test_Module2 as basicdatatypes_test_module2
from tests.hackerrank.basicdatatypes.test_basicdatatypesmain import Test_BasicDataTypeMain as basicdatatypes_main
from tests.hackerrank.introduction.test_module1 import Test_Module1 as introduction_test_module1
from tests.hackerrank.introduction.test_module2 import Test_Module2 as introduction_test_module2
from tests.hackerrank.introduction.test_introductionmain import Test_IntroductionMain as introduction_main

from tests.hackerrank.test_hackerrankmain import Test_HackerRankMain as hackerrank_main

def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.TestLoader().loadTestsFromTestCase(basicdatatypes_test_module1))
    suite.addTest(unittest.TestLoader().loadTestsFromTestCase(basicdatatypes_test_module2))
    suite.addTest(unittest.TestLoader().loadTestsFromTestCase(basicdatatypes_main))
    suite.addTest(unittest.TestLoader().loadTestsFromTestCase(introduction_test_module1))
    suite.addTest(unittest.TestLoader().loadTestsFromTestCase(introduction_test_module2))
    suite.addTest(unittest.TestLoader().loadTestsFromTestCase(introduction_main))
    suite.addTest(unittest.TestLoader().loadTestsFromTestCase(hackerrank_main))
    return suite


if __name__ == '__main__':
    unittest.TextTestRunner(verbosity=2).run(suite())
