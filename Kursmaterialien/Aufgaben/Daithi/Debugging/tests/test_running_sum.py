from unittest import TestCase
import sums as sums


class TestRunning_sum(TestCase):
    """
    here's my first big test class

    """


    def test_running_sum_empty(self):
        """
        test an empty list
        """
        argument = []
        expected = []
        sums.running_sum(argument)
        self.assertEqual(expected,argument,"the list is empty. ")

    def test_running_sum_one_item(self):
        """
         test a one-item list
        """
        argument = [5]
        expected = [5]
        sums.running_sum(argument)
        self.assertEqual(expected, argument,"the list contains one item. ")

    def test_running_sum_two_items(self):
        """
        test a two item list.
        """

        argument = [2,5]
        expected = [2,7]
        sums.running_sum(argument)
        self.assertEqual(expected,argument,"The list contains two items ")

    def test_running_sum_mult_negatives(self):
        """
        test multiple negative values in a list
        """
        argument = [-1,-5,-3,-4]
        expected = [-1,-6,-9,-13]

        sums.running_sum(argument)
        self.assertEqual(expected,argument,"the list contains multuiple negative values")

    def test_running_sum_multi_zeros(self):
        """
        test a list of zeros
        """
        argument = [0,0,0,0]
        expected = [0,0,0,0]
        sums.running_sum(argument)
        self.assertEqual(expected,argument,"the list contains only zeros")

    def test_running_sum_multi_positives(self):
        """
        test a list of positive valuesunittest.main()
        """

        argument = [4,2,3,6]
        expected = [4,6,9,15]
        sums.running_sum(argument)
        self.assertEqual(expected,argument,"the list contains only positive values")

    def test_running_sum_multi_mix(self):
        """
        tests a list containing mixture of negative values, zeros and positive values
        """
        argument = [4,0,2,-5,0]
        expected = [4,4,6,1,1]
        sums.running_sum(argument)
        self.assertEqual(expected,argument, "the list contains a mixture of negative"
                         + "and positive values. ")

