import sys

class largest:
    """
    Return the largest element in a list

    """
    @staticmethod
    def largest_in_list(L):
        """

        :param L: List
        :return: int, the largest number

        """
        # first case we tried :
        #  max = sys.maxsize
        # second case due to error we set
        #  max = 0
        # but we couldn't go below 0, for negative numbers
        # so we set it to min value
        # max = 0
        max = -sys.maxsize -1
        if len(L) == 0:
            raise ValueError("empty list")


        for i in range(len(L)):
            if L[i] > max:
                max = L[i]
        return max



def largest_in_list(L):
        """

        :param L: List
        :return: int, the largest number

        """
        # first case we tried :
        #  max = sys.maxsize
        # second case due to error we set
        #  max = 0
        # but we couldn't go below 0, for negative numbers
        # so we set it to min value
        # max = 0
        max = -sys.maxsize -1
        if len(L) == 0:
            raise ValueError("empty list")


        for i in range(len(L)):
            if L[i] > max:
                max = L[i]
        return max



