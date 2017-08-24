from unittest import TestCase
from largest import largest



class TestLargest(TestCase):

    def test_simple(self):
        """
        test that 9 is the largest from 7,8,9
        :return: true
        """
        self.assertEqual(largest.largest_in_list([7,8,9]),9,"9 is the largest" )

    def test_order(self):
        """
        test the order of a list, if it matters
        :return: true
        """
        self.assertEqual(largest.largest_in_list([9,8,7]), 9,"9 is still largest with different order")
        self.assertEqual(largest.largest_in_list([8,9,7]), 9,"9 is still the largest")
        self.assertEqual(largest.largest_in_list([7,8,9]), 9, "9 is still largest")

    def test_dups(self):
        """
        test for duplicate values
        :return:
        """
        self.assertEqual(largest.largest_in_list([9,7,8,9]),9,"9 duplicated")

    def test_one(self):
        """
        tests for one single value
        :return:
        """
        self.assertEqual(largest.largest_in_list([1]),1,"Only one value")

    def test_negative(self):
        """
        test for negative numbers in a list
        :return:
        """
        self.assertEquals(largest.largest_in_list([-9,-8,-7]),-7,"list of negative numbser")


    def test_empty(self):
        """
        test for an empty string
        :return:
        """
        try:
            largest.largest_in_list([])
            self.fail("Should have thrown an exception")
        except:
            self.assertTrue(True)
