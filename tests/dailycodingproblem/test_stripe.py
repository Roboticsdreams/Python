import unittest
from unittest import mock

from dailycodingproblem import stripe

class TestStripe(unittest.TestCase):
    def setUp(self):
        self.stripeobj = stripe.Stripe()

    def test_firstMissingPositive_Test01(self):
        listinput = [0, 10, 2, -10, -20, 1]
        result = self.stripeobj.firstMissingPositive(listinput)
        expected = 3
        self.assertEqual(result, expected)

    def test_firstMissingPositive_Test02(self):
        listinput = [0]
        result = self.stripeobj.firstMissingPositive(listinput)
        expected = 1
        self.assertEqual(result, expected)

    def test_firstMissingPositive_Test03(self):
        listinput = [10]
        result = self.stripeobj.firstMissingPositive(listinput)
        expected = 1
        self.assertEqual(result, expected)

    def test_firstMissingPositive_Test04(self):
        listinput = [1]
        result = self.stripeobj.firstMissingPositive(listinput)
        expected = 2
        self.assertEqual(result, expected)

    def test_firstMissingPositive_Test05(self):
        listinput = [1, 2, 3, 4, 5]
        result = self.stripeobj.firstMissingPositive(listinput)
        expected = 6
        self.assertEqual(result, expected)

    @mock.patch('dailycodingproblem.stripe.Stripe')
    def test_stripemain(self, mock_Stripe):
        result = stripe.stripemain()
        expected = 1
        self.assertEqual(result, expected)
