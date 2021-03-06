import unittest

from tests.dailycodingproblem.test_airbnb import TestAirbnb
from tests.dailycodingproblem.test_amazon import TestAmazon
from tests.dailycodingproblem.test_apple import TestApple
from tests.dailycodingproblem.test_dailycodingproblemmain import TestDailyCodingProblemMain
from tests.dailycodingproblem.test_facebook import TestFacebook
from tests.dailycodingproblem.test_google import TestGoogle
from tests.dailycodingproblem.test_stripe import TestStripe
from tests.dailycodingproblem.test_twitter import TestTwitter
from tests.dailycodingproblem.test_uber import TestUber


def suite():
    suites = unittest.TestSuite()
    suites.addTest(unittest.TestLoader().loadTestsFromTestCase(TestAirbnb))
    suites.addTest(unittest.TestLoader().loadTestsFromTestCase(TestAmazon))
    suites.addTest(unittest.TestLoader().loadTestsFromTestCase(TestApple))
    suites.addTest(unittest.TestLoader().loadTestsFromTestCase(TestFacebook))
    suites.addTest(unittest.TestLoader().loadTestsFromTestCase(TestGoogle))
    suites.addTest(unittest.TestLoader().loadTestsFromTestCase(TestStripe))
    suites.addTest(unittest.TestLoader().loadTestsFromTestCase(TestTwitter))
    suites.addTest(unittest.TestLoader().loadTestsFromTestCase(TestUber))
    suites.addTest(unittest.TestLoader().loadTestsFromTestCase(TestDailyCodingProblemMain))
    return suites


if __name__ == '__main__':
    unittest.TextTestRunner(verbosity=2).run(suite())